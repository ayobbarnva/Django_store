# 🛒 Django Store

> A modern, responsive e-commerce project built with Django — created as a practical portfolio project.

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-11.1.0-3776AB?style=for-the-badge)

## ✨ About

**Django Store** is a full-stack e-commerce project built with Django. The project focuses on clean architecture, reusable templates, user authentication, product management, profiles, and a functional shopping cart.

It is designed as a learning and portfolio project and can be extended with orders, checkout, payment gateways, REST APIs, and production deployment.

## 🚀 Features

- 🛍️ Product catalog
- 🗂️ Product categories
- 🔎 Product detail pages
- 💰 Product pricing and discounts
- 📦 Stock management
- 🛒 Shopping cart
- ➕ Increase cart quantity
- ➖ Decrease cart quantity
- ❌ Remove products from cart
- 👤 Custom user account
- 🔐 User authentication
- 🖼️ Profile image support
- ✏️ Profile editing
- 📱 Responsive interface
- 🌐 Persian / English language support
- 🌓 Light / dark theme support
- ⚙️ Django Admin for managing products and categories

## 🧰 Tech Stack

| Technology | Usage |
|---|---|
| 🐍 Python | Backend programming |
| 🎯 Django 6.1 | Web framework |
| 🔌 Django REST Framework | API development |
| 🖼️ Pillow | Image handling |
| 🌐 HTML | Templates |
| 🎨 CSS | UI and responsive design |
| ⚡ JavaScript | Frontend interactions |
| 🗄️ SQLite | Development database |

## 📁 Project Structure

```text
Django_store/
├── accouants/          # Custom user / authentication
├── app/                # Products and categories
├── cart/               # Shopping cart
├── profile/            # Profile-related pages
├── project_django/     # Main Django configuration
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ayobbarnva/Django_store.git
cd Django_store
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and keep sensitive values such as `SECRET_KEY` outside Git.

> Never commit your real Django `SECRET_KEY` to a public repository.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🛒 Shopping Cart Flow

```text
Product
   ↓
Add to Cart
   ↓
Cart
   ├── Increase quantity
   ├── Decrease quantity
   └── Remove item
```

## 🔮 Planned Improvements

- 💳 Payment gateway integration
- 📋 Order and checkout system
- 📦 Order history
- ❤️ Wishlist
- 🔍 Advanced product search and filtering
- 🔌 Complete REST API
- 🧪 Automated tests
- 🚀 Production deployment
- 🔐 Environment-based production settings

## 🎯 Project Goal

This project is part of my journey in learning and building real-world Django applications, with a focus on backend development, authentication, database design, e-commerce logic, and clean user interfaces.

## 👨‍💻 Author

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

If you find the project useful, feel free to ⭐ the repository.
