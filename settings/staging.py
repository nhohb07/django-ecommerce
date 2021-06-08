from .base import *
from .setting_utils import get_env_value


ALLOWED_HOSTS = [
    "devblock-django-ecommerce.herokuapp.com",
]
DEBUG = True
SECRET_KEY = get_env_value("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": get_env_value("DB_ENGINE"),
        "NAME": get_env_value("DB_NAME"),
        "USER": get_env_value("DB_USER"),
        "PASSWORD": get_env_value("DB_PASSWORD"),
        "HOST": get_env_value("DB_HOST"),
        "PORT": get_env_value("DB_PORT"),
    }
}

SIMPLE_JWT = BASE_SIMPLE_JWT.update(
    {
        "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
        "SIGNING_KEY": SECRET_KEY,
    }
)
