from django.conf import settings
from rest_framework.serializers import ValidationError

MARK_VALIDATION_ERROR = f'Оценка должна быть целым числом: {settings.MARKS}'


def mark_validator(mark):
    if isinstance(mark, int) and mark in settings.MARKS:
        return mark
    raise ValidationError(MARK_VALIDATION_ERROR)
