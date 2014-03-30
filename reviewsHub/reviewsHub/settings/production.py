DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = os.environ['REVIEWS_HUB_SECRET_KEY']
ALLOWED_HOSTS = ['.schelder.com', '.schelder.com.']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'reviewshub',                      
        'USER': 'hub',
        'PASSWORD': os.environ['REVIEWS_HUB_DB_PASSWD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}
