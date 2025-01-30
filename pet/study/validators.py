import re

from django.conf import settings
from django.core.exceptions import ValidationError

REVIEW_MARK_ERROR = 'Значение оценки должно быть целым числом от 1 до 5'
INVALID_SYMBOLS = r'[^_\w]'
USERNAME_VALIDATOR_MESSAGE = (
    'Найдены недопустимые символы в поле username: '
    '"{invalid_symbols}"'
)


def mark_range(mark):
    if mark < min(settings.MARKS) or mark > max(settings.MARKS):
        raise ValidationError(
            REVIEW_MARK_ERROR
        )


def username_validator(username):
    invalid_symbols = re.findall(INVALID_SYMBOLS, username)
    if invalid_symbols:
        raise ValidationError(
            USERNAME_VALIDATOR_MESSAGE.format(
                invalid_symbols=invalid_symbols
            )
        )
    return username
