from .base import *  # noqa F403
from .base import env, INSTALLED_APPS, MIDDLEWARE

SECRET_KEY = (
    env(
        "DJANGO_SECRET_KEY",
        default="ONg_Ej4_nW8UBp1AOhSu3LZT0NnToX5iyLtSU_x3aptM3ktT4W0",
    ),
)

DEBUG = env.bool("DJANGO_DEBUG", True)

ALLOWED_HOSTS = []

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "test@testemail.com"
