from django.apps import AppConfig

APP_VERBOSE_NAME = 'Настройки проекта'


class ToolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tools'
    verbose_name = APP_VERBOSE_NAME
