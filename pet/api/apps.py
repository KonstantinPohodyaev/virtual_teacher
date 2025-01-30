from django.apps import AppConfig


APP_VERBOSE_NAME = 'api'


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    verbose_name = APP_VERBOSE_NAME
