import os

DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = os.environ['REVIEWS_HUB_SECRET_KEY']
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',                      
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}