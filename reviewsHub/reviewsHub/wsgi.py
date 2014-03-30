"""
WSGI config for reviewsHub project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reviewsHub.settings")

from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()

def application(environ, start_response):
    for key in environ:
        if key.startswith('REVIEWS_HUB_'):
            os.environ[key] = environ[key]
    return _application(environ, start_response)