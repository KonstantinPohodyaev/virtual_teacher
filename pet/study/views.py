from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import CategoryForm, DocumentForm, StudyForm
from .mixins import (CategoryChangeMixin, CategoryFormMixin, CategoryMixin,
                     OnlyAuthorMixin, OnlyStaffCanChange,
                     OnlyTeacherAuthorMixin, ReviewFormMixin, ReviewModelMixin,
                     ReviewURLParamMixin, StudyChangeMixin, StudyFormMixin,
                     StudyMixin)
from .models import Category, Document, Study
from .project_tools import (add_review_info_for_study, filtered_queryset,
                            get_page_object, get_study_avg_rating)


class CustomLogoutView(
    LogoutView
):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class StudyListView(
    StudyMixin, ListView
):
    template_name = 'study/list.html'

    def get_queryset(self):
        user = self.request.user
        status = None
        if user.is_authenticated:
            status = user.status
        return filtered_queryset(
            self.model.objects, is_admin=user.is_staff,
            teacher=status
        )

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(
            **kwargs,
            page_obj=get_page_object(
                add_review_info_for_study(self.get_queryset()),
                settings.STUDY_COUNT_ON_LIST_PAGE,
                self.request.GET.get('page')
            )
        )


class StudyCreateView(
    StudyChangeMixin, StudyFormMixin, OnlyTeacherAuthorMixin, CreateView
):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StudyUpdateView(
    StudyChangeMixin, StudyFormMixin, OnlyTeacherAuthorMixin, UpdateView
):
    pass


class StudyDetailView(
    StudyChangeMixin, DetailView
):
    template_name = 'study/detail.html'

    def dispatch(self, request, *args, **kwargs):
        if (request.user == self.get_object().author
            or (self.get_object().is_published
                and self.get_object().is_on_main)):
            return super().dispatch(request, *args, **kwargs)
        return redirect('study:list')

    def get_context_data(self, **kwargs):
        study = get_object_or_404(
            Study,
            pk=self.kwargs[self.pk_url_kwarg]
        )
        study.avg_rating = get_study_avg_rating(study)
        return super().get_context_data(
            **kwargs,
            study=study,
            page_obj=get_page_object(
                self.get_object().reviews.all(),
                settings.REVIEW_COUNT_ON_DETAIL_STUDY_PAGE,
                self.request.GET.get('page')
            )
        )

    def get_object(self):
        study = super().get_object()
        if self.request.user != study.author:
            redirect('study:list')
        return study


class StudyDeleteView(
    StudyChangeMixin, OnlyTeacherAuthorMixin, DeleteView
):
    template_name = 'study/edit.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            **kwargs,
            form=StudyForm(
                instance=get_object_or_404(
                    Study,
                    pk=self.kwargs[self.pk_url_kwarg]
                )))

    def get_success_url(self):
        return reverse('study:list')


class ReviewCreateView(
    ReviewModelMixin, LoginRequiredMixin, ReviewFormMixin, CreateView
):
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.study = Study.objects.get(id=self.kwargs['study_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'study:detail', args=(self.kwargs['study_id'],)
        ) + '#reviews'


class ReviewUpdateView(
    OnlyAuthorMixin, ReviewURLParamMixin, ReviewFormMixin, UpdateView
):
    def post(self, request, *args, **kwargs):
        review = super().get_object()
        if review.edited is False:
            review.edited = True
            review.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('study:detail', args=(self.kwargs['study_id'],))


class ReviewDeleteView(
    OnlyAuthorMixin, ReviewURLParamMixin, DeleteView
):
    def get_success_url(self):
        return reverse('study:detail', args=(self.kwargs['study_id'],))


class CategoryListView(
    CategoryMixin, LoginRequiredMixin, ListView
):
    template_name = 'study/category_list.html'

    def get_queryset(self):
        return filtered_queryset(
            Category.objects, is_admin=self.request.user.is_staff
        )


class CategoryDetailView(
    CategoryChangeMixin, LoginRequiredMixin, DetailView
):
    template_name = 'study/category_detail.html'


class CategoryCreateView(
    CategoryFormMixin, OnlyStaffCanChange, CreateView
):
    model = Category

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('study:category_list')


class CategoryUpdateView(
    CategoryChangeMixin, CategoryFormMixin, OnlyStaffCanChange, UpdateView
):
    pass


class CategoryDeleteView(CategoryChangeMixin, OnlyStaffCanChange, DeleteView):
    template_name = 'study/category_edit.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            **kwargs,
            form=CategoryForm(
                instance=get_object_or_404(
                    Category,
                    slug=self.kwargs[self.slug_url_kwarg]
                )
            )
        )


def add_documents_for_study(request, study_id):
    study = get_object_or_404(
        Study,
        id=study_id
    )
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            Document.objects.create(
                title=form.cleaned_data['title'],
                study=study,
                file=form.cleaned_data['file']
            )
            return redirect('study:detail', study_id)
    form = DocumentForm()
    return render(
        request,
        'study/add_documents.html',
        {
            'form': form,
            'study': study
        }
    )
