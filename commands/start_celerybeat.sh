#!/bin/bash

rm /currency_exchange/run/celerybeat-schedule
rm /currency_exchange/run/celerybeat.pid
celery -A currency_exchange beat -l info --workdir=/currency_exchange --pidfile=/currency_exchange/run/celerybeat.pid --schedule=/currency_exchange/run/celerybeat-schedule
