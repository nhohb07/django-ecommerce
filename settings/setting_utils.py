import os
from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable_name):
    try:
        return os.environ[env_variable_name]
    except KeyError:
        error_msg = "Please set the {} environment variable".format(env_variable_name)
        raise ImproperlyConfigured(error_msg)
