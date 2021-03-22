import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab7_kolke.settings')

app = Celery('lab7_kolke')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
