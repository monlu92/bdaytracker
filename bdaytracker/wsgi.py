
import django
import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'bdaytracker.settings'
django.setup()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bdaytracker.settings")

application = get_wsgi_application()