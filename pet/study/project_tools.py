from django.core.paginator import Paginator
from django.db.models import Avg, Count
from django.db.models.functions import Round

from .models import TEACHER_STATUS

NO_MARKS_MESSAGE = 'Нет оценок'
RATING_PRECISION_AFTER_COMMA = 2


def filtered_queryset(query_set, is_admin=None, teacher=None):
    if is_admin or teacher == TEACHER_STATUS:
        return query_set.all()
    return query_set.filter(
        is_published=True,
        is_on_main=True
    )


def get_rating(study):
    return sum([review.mark for review in study.reviews.all()])


def get_page_object(queryset, count, page_number):
    return Paginator(
        queryset, count
    ).get_page(page_number)


def add_review_info_for_study(queryset):
    queryset = queryset.annotate(
        rating=Round(
            Avg('reviews__mark'), precision=RATING_PRECISION_AFTER_COMMA
        ),
        reviews_count=Count('reviews')
    )
    return queryset


def get_study_avg_rating(study):
    if get_study_reviews_count(study) == 0:
        return NO_MARKS_MESSAGE
    return (
        round(
            sum(
                [review.mark for review in study.reviews.all()]
            ) / get_study_reviews_count(study), RATING_PRECISION_AFTER_COMMA
        )
    )


def get_study_reviews_count(study):
    return study.reviews.count()
