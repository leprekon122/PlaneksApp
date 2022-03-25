import os
import celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planeks_app.settings")
app = celery.Celery('planeks_app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
