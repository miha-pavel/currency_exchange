#!/bin/bash

rm /currency_exchange/run/celery.pid
celery -A currency_exchange worker -l info --workdir=/currency_exchange --pidfile=/currency_exchange/run/celery.pid
