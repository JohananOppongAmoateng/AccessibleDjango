from django.apps import AppConfig

class AccessibleDjangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accessible_django'

    def ready(self):
        from .checks import img