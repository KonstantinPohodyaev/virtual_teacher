from django.apps import AppConfig

APP_VERBOSE_NAME = 'Учебные материалы'


class StudyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'study'
    verbose_name = APP_VERBOSE_NAME
