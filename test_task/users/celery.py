from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_task_app.settings')

app = Celery('test_task_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_transport_options = {'visibility_timeout': 3600}

app.conf.beat_schedule = {
    'add-order-every-minute': {
        'task': 'myapp.tasks.add_order',
        'schedule': crontab(minute='*/1'),
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
