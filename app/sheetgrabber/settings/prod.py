from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_store',
        'USER': 'db_user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '5432',
    }
}
