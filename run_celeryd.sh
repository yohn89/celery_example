#!/bin/bash
celeryd -B --loglevel=INFO --config=celeryconfig --concurrency=8 
