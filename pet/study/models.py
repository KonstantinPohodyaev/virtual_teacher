from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from .validators import mark_range, username_validator

CUSTOM_USER_USERNAME_VERBOSE_NAME = 'Юзернейм'
CUSTOM_USER_USERNAME_MAX_LENGTH = 128
CUSTOM_USER_USERNAME_HELP_TEXT = 'Придумайте уникальный юзернейм'
CUSTOM_USER_EMAIL_VERBOSE_NAME = 'Адрес электронной почты'
CUSTOM_USER_EMAIL_MAX_LENGTH = 256
CUSTOM_USER_EMAIL_HELP_TEXT = (
    'Введите уникальный адрес электронной почты'
)
CUSTOM_USER_FIRST_NAME_VERBOSE_NAME = 'Имя'
CUSTOM_USER_FIRST_NAME_MAX_LENGTH = 64
CUSTOM_USER_FIRST_NAME_HELP_TEXT = 'Введите ваше имя'
CUSTOM_USER_LAST_NAME_VERBOSE_NAME = 'Фамилия'
CUSTOM_USER_LAST_NAME_MAX_LENGTH = 64
CUSTOM_USER_LAST_NAME_HELP_TEXT = 'Введите вашу фамилию'
CUSTOM_USER_PATRONYMIC_VERBOSE_NAME = 'Отчество'
CUSTOM_USER_PATRONYMIC_MAX_LENGTH = 64
CUSTOM_USER_PATRONYMIC_HELP_TEXT = (
    'Введите ваше отчество или оставьте поле пустым'
)
CUSTOM_USER_STATUS_VERBOSE_NAME = 'Статус'
CUSTOM_USER_STATUS_MAX_LENGTH = 128
CUSTOM_USER_STATUS_HELP_TEXT = (
    'Выберете ваш статус: {statuses}'
)
CUSTOM_USER_VERBOSE_NAME = 'пользователь'
CUSTOM_USER_VERBOSE_NAME_PLURAL = 'Пользователи'

SERVISE_FIELDS_IS_PUBLISHED_VEROBOSE_NAME = 'Публикация'
SERVISE_FIELDS_IS_PUBLISHED_HELP_TEXT = 'Нужно ли опубликовать данный пост?'
SERVISE_FIELDS_IS_ON_MAIN_VEROBOSE_NAME = 'На главной'
SERVISE_FIELDS_IS_ON_MAIN_VEROBOSE_NAME = (
    'Отметьте, отображается ли публикация на главной странице'
)
SERVISE_FIELDS_NAME_VERBOSE_NAME = 'Название'
SERVISE_FIELDS_NAME_MAX_LENGTH = 128
SERVISE_FIELDS_NAME_HELP_TEXT = 'Введите название'
SERVISE_FIELDS_DESCRIPTION_VERBOSE_NAME = 'Описание'
SERVISE_FIELDS_DESCRIPTION_HELP_TEXT = 'Введите название'
SERVISE_FIELDS_SLUG_VERBOSE_NAME = 'Короткое обозначение'
SERVISE_FIELDS_SLUG_MAX_LENGTH = 32
SERVISE_FIELDS_SLUG_HELP_TEXT = 'Введите короткое обозначение'
SERVISE_FIELDS_CREATED_VERBOSE_NAME = 'Время создания'
SERVISE_FIELDS_EDITED_VERBOSE_NAME = 'Время последнего редактирования'

CATEGORY_VERBOSE_NAME = 'категория'
CATEGORY_VERBOSE_NAME_PLURAL = 'Категории'
CATEGORY_DEFAULT_RELATED_NAME = 'categories'
CATEGORY_AUTHOR_VERBOSE_NAME = 'Автор'

STUDY_AUTHOR_HELP_TEXT = 'Укажите автора курса'
STUDY_CATEGORY_HELP_TEXT = 'Укажите, к какой категории относится курс'
STUDY_IMAGE_VERBOSE_NAME = 'Фото'
STUDY_IMAGE_HELP_TEXT = 'Загрузите изображение'

STUDY_VERBOSE_NAME = 'курс'
STUDY_VERBOSE_NAME_PLURAL = 'Курсы'
STUDY_DEFAULT_RELATED_NAME = 'studies'

REVIEW_TEXT_VERBOSE_NAME = 'Текст отзыва'
REVIEW_TEXT_HELP_TEXT = (
    'Оцените работу преподавателей, качество учебных материалов!'
)
REVIEW_MARK_VERBOSE_NAME = 'Оценка'
REVIEW_MARK_HELP_TEXT = (
    'Укажите оценку, на которую вы можете оценить данный курс'
)
REVIEW_IMAGE_VERBOSE_NAME = 'Изображение'
REVIEW_IMAGE_HELP_TEXT = 'Оставьте фото, связанное с прохождением курса!'
REVIEW_AUTHOR_VERBOSE_NAME = 'Автор отзыва'
REVIEW_STUDY_VERBOSE_NAME = 'Курс'
REVIEW_VERBOSE_NAME = 'отзыв'
REVIEW_VERBOSE_NAME_PLURAL = 'Отзывы'
DEFAULT_RELATED_NAME = 'reviews'

DOCUMENT_TITLE_VERBOSE_NAME = 'Название документа'
DOCUMENT_TITLE_MAX_LENGTH = 256
DOCUMENT_TITLE_HELP_TEXT = 'Введите название документа'
DOCUMENT_FILE_VERBOSE_NAME = 'Документ'
DOCUMENT_FILE_HELP_TEXT = 'Загрузите документ'
DOCUMENT_STUDY_VERBOSE_NAME = 'Курс'


TEACHER_STATUS = 'teacher'
STUDENT_STATUS = 'student'


class CustomUser(AbstractUser):
    STATUS_CHOICES = [
        (TEACHER_STATUS, 'Преподаватель'),
        (STUDENT_STATUS, 'Студент')
    ]

    username = models.CharField(
        CUSTOM_USER_USERNAME_VERBOSE_NAME,
        max_length=CUSTOM_USER_USERNAME_MAX_LENGTH,
        unique=True,
        validators=[username_validator],
        help_text=CUSTOM_USER_USERNAME_HELP_TEXT
    )
    email = models.EmailField(
        CUSTOM_USER_EMAIL_VERBOSE_NAME,
        max_length=CUSTOM_USER_EMAIL_MAX_LENGTH,
        unique=True,
        help_text=CUSTOM_USER_EMAIL_HELP_TEXT
    )
    first_name = models.CharField(
        CUSTOM_USER_FIRST_NAME_VERBOSE_NAME,
        max_length=CUSTOM_USER_FIRST_NAME_MAX_LENGTH,
        help_text=CUSTOM_USER_FIRST_NAME_HELP_TEXT
    )
    last_name = models.CharField(
        CUSTOM_USER_LAST_NAME_VERBOSE_NAME,
        max_length=CUSTOM_USER_LAST_NAME_MAX_LENGTH,
        help_text=CUSTOM_USER_LAST_NAME_HELP_TEXT
    )
    patronymic = models.CharField(
        CUSTOM_USER_PATRONYMIC_VERBOSE_NAME,
        max_length=CUSTOM_USER_PATRONYMIC_MAX_LENGTH,
        blank=True,
        null=True,
        help_text=CUSTOM_USER_PATRONYMIC_HELP_TEXT
    )
    status = models.CharField(
        CUSTOM_USER_STATUS_VERBOSE_NAME,
        max_length=CUSTOM_USER_STATUS_MAX_LENGTH,
        choices=STATUS_CHOICES,
        help_text=CUSTOM_USER_STATUS_HELP_TEXT.format(
            statuses=[status[1] for status in STATUS_CHOICES]
        )
    )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = CUSTOM_USER_VERBOSE_NAME
        verbose_name_plural = CUSTOM_USER_VERBOSE_NAME_PLURAL
        ordering = ['username', 'last_name', 'first_name']


class BaseDataTimeFields(models.Model):
    created = models.DateTimeField(
        SERVISE_FIELDS_CREATED_VERBOSE_NAME,
        auto_now_add=True,
    )
    edit = models.DateTimeField(
        SERVISE_FIELDS_EDITED_VERBOSE_NAME,
        auto_now=True
    )

    class Meta:
        abstract = True
        default_related_name = '%(class)ss'


class ServiseFields(models.Model):
    is_published = models.BooleanField(
        SERVISE_FIELDS_IS_PUBLISHED_VEROBOSE_NAME,
        help_text=SERVISE_FIELDS_IS_PUBLISHED_HELP_TEXT,
    )

    is_on_main = models.BooleanField(
        SERVISE_FIELDS_IS_ON_MAIN_VEROBOSE_NAME,
        help_text=SERVISE_FIELDS_IS_ON_MAIN_VEROBOSE_NAME
    )
    name = models.CharField(
        SERVISE_FIELDS_NAME_VERBOSE_NAME,
        max_length=SERVISE_FIELDS_NAME_MAX_LENGTH,
        unique=True,
        help_text=SERVISE_FIELDS_NAME_HELP_TEXT
    )
    description = models.TextField(
        SERVISE_FIELDS_DESCRIPTION_VERBOSE_NAME,
        blank=True,
        null=True,
        help_text=SERVISE_FIELDS_DESCRIPTION_HELP_TEXT
    )
    slug = models.SlugField(
        SERVISE_FIELDS_SLUG_VERBOSE_NAME,
        unique=True,
        max_length=SERVISE_FIELDS_SLUG_MAX_LENGTH,
        help_text=SERVISE_FIELDS_SLUG_HELP_TEXT
    )

    class Meta:
        abstract = True
        default_related_name = '%(class)ss'

    def __str__(self):
        return self.name[:50]


class Category(ServiseFields, BaseDataTimeFields):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=CATEGORY_AUTHOR_VERBOSE_NAME
    )

    class Meta:
        verbose_name = CATEGORY_VERBOSE_NAME
        verbose_name_plural = CATEGORY_VERBOSE_NAME_PLURAL
        default_related_name = CATEGORY_DEFAULT_RELATED_NAME
        ordering = ['name', 'created']


class Study(ServiseFields, BaseDataTimeFields):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        help_text=STUDY_AUTHOR_HELP_TEXT
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text=STUDY_CATEGORY_HELP_TEXT
    )
    image = models.ImageField(
        STUDY_IMAGE_VERBOSE_NAME,
        upload_to=settings.STUDY_IMAGE_UPLOAD_TO,
        blank=True,
        help_text=STUDY_IMAGE_HELP_TEXT,
    )

    class Meta:
        verbose_name = STUDY_VERBOSE_NAME
        verbose_name_plural = STUDY_VERBOSE_NAME_PLURAL
        default_related_name = 'studies'
        ordering = ['name', 'created']

    def get_absolute_url(self):
        return reverse('study:detail', args=[self.pk])


class Document(models.Model):
    title = models.CharField(
        DOCUMENT_TITLE_VERBOSE_NAME,
        max_length=DOCUMENT_TITLE_MAX_LENGTH,
        help_text=DOCUMENT_TITLE_HELP_TEXT
    )
    file = models.FileField(
        DOCUMENT_FILE_VERBOSE_NAME,
        upload_to=settings.DOCUMENT_FILE_UPLOAD_TO,
        help_text=DOCUMENT_FILE_HELP_TEXT
    )
    study = models.ForeignKey(
        Study,
        on_delete=models.CASCADE,
        verbose_name=DOCUMENT_STUDY_VERBOSE_NAME
    )


class Review(BaseDataTimeFields):
    text = models.TextField(
        REVIEW_TEXT_VERBOSE_NAME,
        help_text=REVIEW_TEXT_HELP_TEXT
    )
    mark = models.IntegerField(
        REVIEW_MARK_VERBOSE_NAME,
        validators=(mark_range,),
        help_text=REVIEW_MARK_HELP_TEXT
    )
    image = models.ImageField(
        REVIEW_IMAGE_VERBOSE_NAME,
        upload_to=settings.REVIEW_IMAGE_UPLOAD_TO,
        blank=True,
        help_text=REVIEW_IMAGE_HELP_TEXT
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=REVIEW_AUTHOR_VERBOSE_NAME
    )
    study = models.ForeignKey(
        Study,
        on_delete=models.CASCADE,
        verbose_name=REVIEW_STUDY_VERBOSE_NAME
    )

    class Meta(BaseDataTimeFields.Meta):
        verbose_name = REVIEW_VERBOSE_NAME
        verbose_name_plural = REVIEW_VERBOSE_NAME_PLURAL
        ordering = ['-created']

    def __str__(self):
        return f'{self.mark}: {self.text[:40]}'
