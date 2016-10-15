import os
from os.path import abspath, dirname, join

CONFIG_ROOT = dirname(dirname(abspath(__file__)))

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.prod"

exec(open(join(dirname(CONFIG_ROOT), ".env-prod.py")).read())

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
