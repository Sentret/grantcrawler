
import os
import django
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grant_module.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
