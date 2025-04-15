from django.apps import AppConfig


class AboutusConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.aboutus"

    def ready(self):
        import apps.aboutus.signals  # noqa: 401
