# project/config.py

import os
try:
    # Python 2.7
    import ConfigParser as configparser
except ImportError:
    # Python 3
    import configparser

basedir = os.path.abspath(os.path.dirname(__file__))


def _get_bool_env_var(varname, default=None):

    value = os.environ.get(varname, default)

    if value is None:
        return False
    elif isinstance(value, str) and value.lower() == 'false':
        return False
    elif bool(value) is False:
        return False
    else:
        return bool(value)


class BaseConfig(object):
    """Base configuration."""

    # main config
    SECRET_KEY = 'my_precious'
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # mail settings
    # defaults are:
    #  - MAIL_SERVER = 'smtp.googlemail.com'
    #  - MAIL_PORT = 465
    #  - MAIL_USE_TLS = False
    #  - MAIL_USE_SSL = True
    MAIL_SERVER = os.environ.get('APP_MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('APP_MAIL_PORT', 465))
    MAIL_USE_TLS = _get_bool_env_var('APP_MAIL_USE_TLS', False)
    MAIL_USE_SSL = _get_bool_env_var('APP_MAIL_USE_SSL', True)

    # mail authentication
    MAIL_USERNAME = os.environ.get('APP_MAIL_USERNAME', None)
    MAIL_PASSWORD = os.environ.get('APP_MAIL_PASSWORD', None)

    # mail accounts
    MAIL_DEFAULT_SENDER = 'Smilar@org.com'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG_TB_ENABLED = True