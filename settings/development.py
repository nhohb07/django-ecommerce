from .base import *

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
DEBUG = True
SECRET_KEY = "dev@secret#1938"


DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecommerce',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SIMPLE_JWT.update(
    {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        "SIGNING_KEY": SECRET_KEY,
    }
)


