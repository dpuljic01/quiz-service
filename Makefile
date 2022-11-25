run:
	@python manage.py runserver 8000

superuser:
	@python manage.py createsuperuser

migrations:
	@python manage.py makemigrations

test:
	@python manage.py test

