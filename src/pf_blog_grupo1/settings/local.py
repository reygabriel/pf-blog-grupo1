from .base import *

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pf_blog',
        'USER': 'root',
        'PASSWORD': 'RZmg+1995',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
