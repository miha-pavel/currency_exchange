# Hillel currency_exchange
Studying django students tracker.

This project supposed to run on `python3`


## Location
This site locate [GitHub Pages](https://github.com/miha-pavel/currency_exchange)


## Before first launchac
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
```docker-compose up -d```
2. Посмотреть активные контейнеры
```docker ps -a``` или ```docker-compose ps```
3. Выполнение команды внутри контейнера
```docker exec -it <command>```
   - Например выполнить миграции внутри контейнера
    ```docker exec -it django ./manage.py makemigrations```
    ```docker exec -it django ./manage.py migrate```
    ```docker exec -it django ./manage.py createsuperuser```
   - Зайти в терминал контейнера джанго
    ```docker exec -it django bash```
4. kill all conteiner (for Mac)
```docker ps -q | xargs docker stop ; docker system prune -a```
5. Просматриваем логи в контейнера.
    копируем CONTAINER ID полученные, ```docker ps -a``` CONTAINER_ID
```docker logs <CONTAINER_ID>```
6. Проинспектировать контейнер c CONTAINER_ID
```docker inspect <CONTAINER_ID>```
7. Рестарт отдельного контейнера conteiner_name
```docker restart <conteiner_name>```
8. You can check which values are assigned to the environment variables
```docker-compose config```
9. Restart all running containers:
```docker restart $(docker ps -q)```
10. Stop или Start отдельных контейнеров,
    например, сразу два контейнера "celery_worker" и "celery_beat"
```docker-compose stop celery_beat```
```docker-compose start celery_worker celery_beat```
11. Посмотреть какие имеджи запущенны
```docker images```


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


### Домашнее задание 17
Добавлено: 21.02.2020 16:53
Реализовать 5 парсеров
1. [x] Курс по Монобанк
2. [x] Курс по сайту http://vkurse.dp.ua/. 
Для парсинга данных можно использовать
https://www.crummy.com/software/BeautifulSoup/bs4/doc/.
https://www.dataquest.io/blog/web-scraping-tutorial-python/
3. [x] Найти и собрать данные с еще 3х источников.


### Домашнее задание 18
Добавлено: 01.03.2020 19:52
Добавить форму обартной связи
1. [x] Форма должна иметь три поля: email, title, text
2. [x] Письмо должно быть отправленно с помощью celery
3. [x] Записывать каждое отправленное письмо в базу данных. Модель Contact. Поля: email, title, text, created (время создания записи)
4. [x] Использовать Class Based Views


https://riptutorial.com/ru/django/example/11709/django-class-based-views--%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-createview


https://ccbv.co.uk/


https://ccbv.co.uk/projects/Django/3.0/django.views.generic.edit/CreateView/


### Домашнее задание 19
Добавлено: 06.03.2020 19:29
Реализовать функционал
1. [x] Добавить вкладку слева Latest Rates
2. [x] Вывести последние 20 записей из таблицы Rate использовав bootstrap таблицу. Таблицу выбрать самостоятельно.
3. [x] Необходимо использовать cbv ListView.


Дополнительно задание.

Добавить вкладки login/logout/my profile

Добавить возможность редактировать только свой профиль. Вкладки logout/my profile должны быть доступны только для залогиненых юзеров. Login только для анонимных пользователей


### Домашнее задание 20
Добавлено: 13.03.2020 18:05
Реализовать функционал
1. [x] Удалят файлы с диска (медиа файлы) когда они изменены или были удалены. (Можно использовать джанго сигналы)
2. [x] Написать команду которая спарсит курс за последние 4 года и запишет в базу. Проследить за полем created.

(https://api.privatbank.ua/#p24/exchangeArchive)

### Домашнее задание 22
Добавлено: 23.03.2020 11:21
Создать флоу реистрации с помощью СМС.
Сделать задание в отдельной ветке. Пул реквест НЕ мерджить.

1. [x] Форма регистрации должна содержать след. поля: email, username, phone, password, password2
2. [x] Создать модель ActivationCodeSMS.
3. [x] Форма подтверждения кода.

Код должен содержать не менее 4х случайных целых числа.


### Домашнее задание 23
Добавлено: 27.03.2020 14:14
Реализовать функционал
1. [x] Добавить фильтрацию на вью /rates/ GET. Поля для фильтрации: created - exact, lt, lte, gt, gte + BONUS range, source - exact, currency - exact
2. [x] Реалтзовать функционал для ContactUs модели по аналогии rates. Отсылать письмо при сохранении обькта в базу. Показывать только записи связанные с request юзером.
3. [x] BONUS, добавть юнит тесты для АПИ.
