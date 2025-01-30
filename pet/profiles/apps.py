from django.apps import AppConfig

APP_VERBOSE_NAME = 'Профили'


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    verbose_name = 'Профили'
