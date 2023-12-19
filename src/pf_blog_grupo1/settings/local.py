from .base import *

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blognueva',
        'USER': 'root',
        'PASSWORD': 'administrador',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
