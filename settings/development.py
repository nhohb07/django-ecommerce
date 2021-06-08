from .base import *

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
DEBUG = True
SECRET_KEY = "dev@secret#1938"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SIMPLE_JWT.update(
    {
        "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
        "SIGNING_KEY": SECRET_KEY,
    }
)
