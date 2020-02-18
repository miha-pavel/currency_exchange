run:
	./manage.py runserver

test:
	./manage.py test --keepdb

check:
	./check.sh

pep8:
	flake8

sh_p:
	./manage.py shell_plus

migrate:
	./manage.py migrate

celery:
	celery -A currency_exchange worker -l info

celery_beat:
	celery -A currency_exchange beat -l info

rabbit:
	rabbitmq-server

dc:
	docker-compose -f dc.yml up -d
