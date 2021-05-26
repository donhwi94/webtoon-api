import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    ".ap-northeast-2.compute.amazonaws.com",
    "3.35.168.239",
]

STATIC_ROOT = BASE_DIR / "static/"

STATICFILES_DIRS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}
