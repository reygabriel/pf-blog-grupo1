from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rgabi1219$blog_db',
        'USER': 'rgabi1219',
        'PASSWORD': 'Gabi+1995',
        'HOST': 'rgabi1219.mysql.pythonanywhere-services.com',
        'PORT': '3306'
    }
}