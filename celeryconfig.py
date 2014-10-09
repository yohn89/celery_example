#encoding:utf-8
#from task import tasks
import celery
from datetime import timedelta
from celery.schedules import crontab

CELERY_TIMEZONE = 'US/Eastern'
CELERY_IMPORTS                = ("tasks",)
BROKER_TRANSPORT              = "redis"
BROKER_URL                    = 'redis://127.0.0.1:6379/2'

CELERY_RESULT_BACKEND         = "redis://127.0.0.1:6379/2"
CELERY_REDIS_BACKEND_SETTINGS = { 'host':'127.0.0.1', 'port':6379, } 

CELERYBEAT_SCHEDULE = {

    # timedelta

    #"t1": {
    #    "task": "tasks.add",
    #    "schedule":timedelta(minutes=1),
    #},
    
    # crontab

    #"t2": {
    #    "task": "tasks.add",
    #    "schedule":crontab(minute='1',hour='20'),
    #},


}

