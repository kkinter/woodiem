from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "woodiem.profiles"

    def ready(self):
        from woodiem.profiles import signals  # noqa F401
