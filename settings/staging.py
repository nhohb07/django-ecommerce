from .base import *
from .setting_utils import get_env_value


ALLOWED_HOSTS = [
    "devblock-django-ecommerce.herokuapp.com",
]
DEBUG = False
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

SIMPLE_JWT.update(
    {
        "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
        "SIGNING_KEY": SECRET_KEY,
    }
)


AWS_ACCESS_KEY_ID = get_env_value('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_value('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_env_value('BUCKET_NAME')
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = get_env_value('AWS_S3_REGION_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = False
DEFAULT_FILE_STORAGE = get_env_value('DEFAULT_FILE_STORAGE')
