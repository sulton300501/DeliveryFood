import os

import environ
from celery import Celery

from django.conf import settings

env = environ.Env()
env.read_env(".env")


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env.str("DJANGO_SETTINGS_MODULE"))

app = Celery("core")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks(packages=settings.INSTALLED_APPS)
