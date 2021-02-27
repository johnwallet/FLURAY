import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FLURAY.settings')

app = Celery('FLURAY')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_curse': {
        'task': 'personalaccount.tasks.update_curse',
        'schedule': crontab(minute='*'),
    },
    'update_partner_line': {
        'task': 'personalaccount.tasks.update_partner_line',
        'schedule': crontab(minute=0, hour=1),
    }
}

