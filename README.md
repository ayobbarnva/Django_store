# Django Store

A responsive Django e-commerce project with bilingual Persian/English interface support and light/dark mode.

## Features

- Product catalog with categories
- Product details and discounted prices
- Shopping cart with quantity controls
- User registration, login, profile and profile editing
- Persian / English language switcher
- Light / dark theme switcher
- Responsive interface for mobile and desktop

## Technologies

- Python
- Django
- HTML, CSS and JavaScript
- SQLite
- Pillow

## Installation

```bash
git clone https://github.com/ayobbarnva/django-store.git
cd django-store

python -m venv .venv
source .venv/bin/activate

pip install django pillow

python manage.py migrate
python manage.py runserver
