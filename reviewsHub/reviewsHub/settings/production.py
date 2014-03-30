import os

DEBUG = True
TEMPLATE_DEBUG = True
SECRET_KEY = os.getenv('REVIEWS_HUB_SECRET_KEY')
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