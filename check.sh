#! /bin/bash

python manage.py check
flake8
python manage.py test --keepdb
pip check