# Hillel currency_exchange
Studying django students tracker.

This project supposed to run on `python3`


## Location
This site locate [GitHub Pages](https://github.com/miha-pavel/currency_exchange)


## Before first launch
```
1. python3 -m venv env
2. . env/bin/activate
3. pip install -r requirements.txt
4. Configure project using `local_conf_example.py` as example. Your local settings should be written in `local_conf.py`
5. python manage.py migrate
```


## Run Django project
```
python manage.py runserver
```

Or use makefile guide


## Makefile guide
* ```make run``` - will run Django developer server at 8000 port
* ```make test``` - will test the project with --keepdb option
* ```make pep8``` - will check the code with pylint
* ```make check``` - will check
* ```make sh_p``` - will run django shell_plus
* ```make migrate``` - will run django "./manage.py migrate" command
* ```make celery``` - will run celery
* ```make celery_beat``` - will run celerybeat
* ```make rabbit``` - will run rabbitmq brocker


## Default super user
* Username: admin
* Email address: admin@admin.com
* Password: admin


### Домашнее задание 