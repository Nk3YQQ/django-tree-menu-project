run:
	docker-compose up --build

run-test:
	docker-compose -f docker-compose.dev.yml up --build -d

entrypoint:
	python3 manage.py migrate
	python3 manage.py csu
	python3 manage.py collectstatic --noinput
	gunicorn --config gunicorn_config.py config.wsgi:application

linters:
	docker-compose -f docker-compose.dev.yml exec -T app flake8 config/
	docker-compose -f docker-compose.dev.yml exec -T app flake8 users/

stop:
	docker-compose down

clean-test:
	docker-compose -f docker-compose.dev.yml down --volumes
