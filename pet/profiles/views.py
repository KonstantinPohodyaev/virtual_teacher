from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from study.models import CustomUser, Study
from study.project_tools import (add_review_info_for_study, filtered_queryset,
                                 get_page_object)


class ProfileListView(ListView, LoginRequiredMixin):
    model = CustomUser
    paginate_by = 4
    template_name = 'profiles/list.html'


class ProfileDetailView(DetailView, LoginRequiredMixin):
    model = CustomUser
    template_name = 'profiles/detail.html'
    slug_url_kwarg = 'username'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            **kwargs,
            page_obj=get_page_object(
                add_review_info_for_study(filtered_queryset(Study.objects)),
                settings.STUDY_COUNT_ON_LIST_PAGE,
                self.request.GET.get('page')
            ),
            categories=filtered_queryset(
                self.get_object().categories.all()
            )
        )
