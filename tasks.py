import os

from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv

from api import update_contacts

load_dotenv()

app = Celery('tasks', broker=os.environ.get("CELERY_BROKER_URL"))

app.conf.beat_schedule = {
    'update-contacts-every-minute': {
        'task': 'tasks.update_contacts_task',
        'schedule': crontab(minute="*"),  #  every minute 'minute="*"', every day 'minute="0", hour="0"'
    },
}


@app.task
def update_contacts_task():
    update_contacts()
