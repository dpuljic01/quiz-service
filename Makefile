run:
	@python manage.py runserver 8000

shell:
	@python manage.py shell

superuser:
	@python manage.py createsuperuser

migrations:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

test:
	@python manage.py test

install:
	@pip install -r requirements.txt -U
