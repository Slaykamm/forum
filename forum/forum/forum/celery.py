import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forum.settings')
 
app = Celery('forum')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'WeeklyNewsUpdate2': {
        'task': 'posts.tasks.weeklyUpdates',
#        'schedule': crontab(),
        'schedule': crontab(hour=20, minute=11, day_of_week='Wednesday'),
#        'args': (5,),
    },
}
