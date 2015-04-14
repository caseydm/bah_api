"""
WSGI config for bahproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bahproject.settings")

application = get_wsgi_application()

# added setup files for Heroku

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)