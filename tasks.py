#encoding:utf-8

"""
Some celery tasks here

"""

import celery 
import celeryconfig 
from logger import getlogger

logger  = getlogger(__name__)
app     = celery.Celery() 
app.config_from_object(celeryconfig)

@app.task
def add(x, y):
    """
    return x + y

    """
    z = x + y
    logger.info('{} + {} = {}'.format(x, y, z))
    return 'done', z
