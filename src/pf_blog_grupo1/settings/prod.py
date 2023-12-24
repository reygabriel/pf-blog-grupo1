from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inf0bl0g$blog_db',
        'USER': 'inf0bl0g',
        'PASSWORD': 'ongamolrac',
        'HOST': 'inf0bl0g.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}