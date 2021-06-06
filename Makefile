DEV_ENV=\
	DJANGO_SETTINGS_MODULE=settings.development

start:
	$(DEV_ENV) python manage.py runserver

makemigrations:
	$(DEV_ENV) python manage.py makemigrations

migrate:
	$(DEV_ENV) python manage.py migrate
