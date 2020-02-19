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
* ```make dc``` - will run docker-compose


## Default super user
* Username: admin
* Email address: admin@admin.com
* Password: admin


## DOCKER commands
1. Запуск контейнеризации
```docker-compose -f dc.yml up -d```
2. Посмотреть активные контейнеры
```docker ps -a или docker-compose -f dc.yml ps```
3. Запуск терминала внутри контейнера
```docker exec -it rabbitmq bash ```
4. kill all conteiner (for Mac)
```docker ps -q | xargs docker stop ; docker system prune -a```
5. Просматриваем информацию о контейнерах
```docker ps -a```
6. Просматриваем логи в контейнера.
    копируем CONTAINER ID полученные, ```docker ps -a``` CONTAINER_ID
```docker logs <CONTAINER_ID>```
7. Проинспектировать контейнер c CONTAINER_ID
```docker inspect <CONTAINER_ID>```
8. Рестарт отдельного контейнера conteiner_name
```docker restart <conteiner_name>```


### Домашнее задание 15
Добавлено: 14.02.2020 16:30
login/logout
Необходимо добавить функционал

1. [x] [Логин - логаут] (https://learndjango.com/tutorials/django-login-and-logout-tutorial)
2. [x] [Регистрация] (https://learndjango.com/tutorials/django-signup-tutorial)
3. [x] [Сброс пароля] (https://learndjango.com/tutorials/django-password-reset-tutorial)


### Домашнее задание 16
Добавлено: 17.02.2020 11:12

1. [x] Докерезировать [джанго] (https://docs.docker.com/compose/django/) приложение.
2. [x] Докерезировать селери и селерибит.