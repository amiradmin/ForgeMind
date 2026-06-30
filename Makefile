.PHONY: install format lint check test run migrate makemigrations shell

install:
	cd backend && pip install -r requirements/development.txt

format:
	cd backend && isort .
	cd backend && black .

lint:
	cd backend && ruff check .

check:
	cd backend && python manage.py check

test:
	cd backend && pytest

run:
	cd backend && python manage.py runserver

migrate:
	cd backend && python manage.py migrate

makemigrations:
	cd backend && python manage.py makemigrations

shell:
	cd backend && python manage.py shell