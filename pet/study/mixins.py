from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import CategoryForm, ReviewForm, StudyForm
from .models import TEACHER_STATUS, Category, Review, Study


STUDY_MIXIN_PAGINATE_BY = 4


class OnlyTeacherAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return (
            user == self.get_object().author
            and user.status == TEACHER_STATUS
            or user.is_staff
        )


class OnlyAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return (
            user == self.get_object().author
            or user.is_staff
        )


class OnlyStaffCanChange(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class StudyMixin:
    model = Study
    paginate_by = STUDY_MIXIN_PAGINATE_BY


class StudyChangeMixin:
    model = Study
    pk_url_kwarg = 'study_id'


class StudyFormMixin:
    form_class = StudyForm
    template_name = 'study/edit.html'


class CategoryMixin:
    model = Category
    paginate_by = settings.CATEGORY_COUNT_ON_LIST_PAGE


class CategoryChangeMixin:
    model = Category
    slug_field = 'slug'
    slug_url_kwarg = 'category_slug'


class CategoryFormMixin:
    template_name = 'study/category_edit.html'
    form_class = CategoryForm


class ReviewModelMixin:
    model = Review
    template_name = 'study/review_edit.html'


class ReviewURLParamMixin:
    model = Review
    pk_url_kwarg = 'review_id'


class ReviewFormMixin:
    form_class = ReviewForm
