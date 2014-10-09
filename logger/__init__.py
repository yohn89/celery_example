#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
log
~~~

This module customize the logging handler so that we can acheive a colorful output

Usage:

>>> import log
>>> logger = log.getlogger("TestLogger")
>>> logger.info("this is some information")
[time]<TestLogger>INFO:this is some  information

"""

import os
import logging
from ansistrm import ColorizingStreamHandler
LOG_LEVEL =  logging.DEBUG

handler = ColorizingStreamHandler()
handler.setFormatter(logging.Formatter("[%(asctime)s]<%(name)s>%(levelname)s:%(message)s", None))
handler.setLevel(logging.DEBUG)

root = logging.getLogger()
root.addHandler(handler)

import logging.handlers

def getlogger(name, level=LOG_LEVEL):
    base_path = '/tmp/celery_example/'
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    filename = os.path.join(base_path,'main.log')
    logger = logging.getLogger(name)
    handler = logging.handlers.RotatingFileHandler(filename, maxBytes=2**30, backupCount=10)
    handler.setFormatter(logging.Formatter("[%(asctime)s]<%(name)s>%(levelname)s:%(message)s", None))
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
