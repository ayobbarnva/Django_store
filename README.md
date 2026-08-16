# 🛒 Django Store

> A modern, responsive bilingual e-commerce store built with Django as a practical portfolio project.

🇬🇧 [English](README.md) | 🇮🇷 [فارسی](README.fa.md)

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-11.1.0-3776AB?style=for-the-badge)

---

## ✨ About

**Django Store** is a full-stack e-commerce project built with Django. It focuses on practical web development concepts such as user management, authentication, products, categories, profiles, and shopping cart logic.

## 🚀 Features

- 🛍️ Product catalog
- 🗂️ Categories
- 🔎 Product details
- 💰 Pricing & discounts
- 📦 Stock management
- 🛒 Shopping cart
- ➕ Increase quantity
- ➖ Decrease quantity
- ❌ Remove items
- 👤 Custom user system
- 🔐 Authentication
- 🖼️ Profile images
- ✏️ Profile editing
- 📱 Responsive UI
- 🌐 Persian / English support
- 🌓 Light / Dark mode
- ⚙️ Django Admin

## 🧰 Tech Stack

| Technology | Usage |
|---|---|
| 🐍 Python | Backend |
| 🎯 Django 6.1 | Web Framework |
| 🔌 Django REST Framework | API development |
| 🖼️ Pillow | Image handling |
| 🌐 HTML | Templates |
| 🎨 CSS | UI |
| ⚡ JavaScript | Frontend interactions |
| 🗄️ SQLite | Development database |

## 📁 Project Structure

```text
Django_store/
├── accouants/
├── app/
├── cart/
├── profile/
├── project_django/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/ayobbarnva/Django_store.git
cd Django_store
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows:

```powershell
.venv\Scripts\activate
```

## 🔐 Environment Variables

Create a `.env` file and keep sensitive values such as `SECRET_KEY` outside Git.

> ⚠️ Never commit your real Django `SECRET_KEY` to a public repository.

## 🗄️ Migrations

This project uses multiple Django apps. When a model changes, you can create migrations for the specific app:

```bash
python manage.py makemigrations accouants
python manage.py makemigrations app
python manage.py makemigrations cart
python manage.py makemigrations profile
```

Or detect changes across all installed apps:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

## 👤 Create Admin

```bash
python manage.py createsuperuser
```

## ▶️ Run

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🛒 Shopping Cart

```text
Product
   ↓
Add to Cart
   ↓
Cart
   ├── ➕ Increase quantity
   ├── ➖ Decrease quantity
   └── ❌ Remove item
```

## 🔮 Future Improvements

- 💳 Payment gateway
- 📋 Orders & Checkout
- 📦 Order history
- ❤️ Wishlist
- 🔍 Advanced search & filtering
- 🔌 Complete REST API
- 🧪 Automated tests
- 🚀 Production deployment
- 🔐 Production settings

## 🎯 Goal

This project is part of my journey in building real-world Django applications, focusing on backend development, authentication, database design, e-commerce logic, and user interface design.

## 👨‍💻 Author

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

⭐ If you find the project useful, give it a star.
