# 🛒 Django Store

> A modern, responsive bilingual e-commerce store built with Django as a practical portfolio project.

> 🇮🇷 **فارسی:** یک فروشگاه اینترنتی مدرن، Responsive و دو زبانه که با Django ساخته شده و به‌عنوان پروژه عملی و نمونه‌کار توسعه داده شده است.

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-11.1.0-3776AB?style=for-the-badge)

---

## ✨ About | درباره پروژه

### 🇬🇧 English

**Django Store** is a full-stack e-commerce project built with Django. It focuses on practical web development concepts such as user management, authentication, products, categories, profiles, and shopping cart logic.

### 🇮🇷 فارسی

**Django Store** یک پروژه فروشگاه اینترنتی Full-Stack ساخته‌شده با Django است که روی مدیریت کاربران، احراز هویت، محصولات، دسته‌بندی‌ها، پروفایل و منطق سبد خرید تمرکز دارد.

## 🚀 Features | امکانات

- 🛍️ Product catalog — نمایش محصولات
- 🗂️ Categories — دسته‌بندی محصولات
- 🔎 Product details — صفحه جزئیات محصول
- 💰 Pricing & discounts — قیمت و تخفیف
- 📦 Stock management — مدیریت موجودی
- 🛒 Shopping cart — سبد خرید
- ➕ Increase quantity — افزایش تعداد
- ➖ Decrease quantity — کاهش تعداد
- ❌ Remove items — حذف محصول
- 👤 Custom user system — سیستم کاربری اختصاصی
- 🔐 Authentication — ثبت‌نام و ورود
- 🖼️ Profile images — تصویر پروفایل
- ✏️ Profile editing — ویرایش پروفایل
- 📱 Responsive UI — طراحی Responsive
- 🌐 Persian / English — پشتیبانی فارسی و انگلیسی
- 🌓 Light / Dark mode — حالت روشن و تاریک
- ⚙️ Django Admin — مدیریت محصولات و دسته‌بندی‌ها

## 🧰 Tech Stack | تکنولوژی‌ها

| Technology | کاربرد |
|---|---|
| 🐍 Python | Backend |
| 🎯 Django 6.1 | Web Framework |
| 🔌 Django REST Framework | توسعه API |
| 🖼️ Pillow | مدیریت تصاویر |
| 🌐 HTML | Templates / قالب‌ها |
| 🎨 CSS | UI / رابط کاربری |
| ⚡ JavaScript | Frontend interactions / تعاملات |
| 🗄️ SQLite | Development database / پایگاه داده توسعه |

## 📁 Project Structure | ساختار پروژه

```text
Django_store/
├── accouants/          # Users & authentication / کاربران و احراز هویت
├── app/                # Products & categories / محصولات و دسته‌بندی‌ها
├── cart/               # Shopping cart / سبد خرید
├── profile/            # User profiles / پروفایل کاربران
├── project_django/     # Main Django configuration / تنظیمات اصلی
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation | نصب و اجرا

Clone the repository / دریافت پروژه:

```bash
git clone https://github.com/ayobbarnva/Django_store.git
cd Django_store
```

Create a virtual environment / ساخت محیط مجازی:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies / نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables | متغیرهای محیطی

Create a `.env` file and keep sensitive values such as `SECRET_KEY` outside Git.

یک فایل `.env` بسازید و اطلاعات حساس مانند `SECRET_KEY` را خارج از Git نگه دارید.

> ⚠️ Never commit your real Django `SECRET_KEY` to a public repository.
>
> ⚠️ کلید واقعی Django را داخل Repository عمومی قرار ندهید.

## 🗄️ Migrations | Migrationها

This project uses multiple Django apps. When a model changes, you can create migrations for the specific app.

این پروژه از چند Django App تشکیل شده است. در صورت تغییر Modelهای هر App می‌توانید Migration همان App را جداگانه ایجاد کنید:

```bash
python manage.py makemigrations accouants
python manage.py makemigrations app
python manage.py makemigrations cart
python manage.py makemigrations profile
```

Or detect changes across all installed apps:

یا همه Appها را یکجا بررسی کنید:

```bash
python manage.py makemigrations
```

Apply migrations / اعمال Migrationها:

```bash
python manage.py migrate
```

## 👤 Create Admin | ساخت ادمین

```bash
python manage.py createsuperuser
```

## ▶️ Run | اجرای پروژه

```bash
python manage.py runserver
```

Open / سپس باز کنید:

```text
http://127.0.0.1:8000/
```

## 🛒 Shopping Cart | سبد خرید

```text
Product
   ↓
Add to Cart
   ↓
Cart
   ├── ➕ Increase quantity / افزایش تعداد
   ├── ➖ Decrease quantity / کاهش تعداد
   └── ❌ Remove item / حذف محصول
```

## 🔮 Future Improvements | امکانات آینده

- 💳 Payment gateway — درگاه پرداخت
- 📋 Orders & Checkout — سفارش و Checkout
- 📦 Order history — تاریخچه سفارش‌ها
- ❤️ Wishlist — علاقه‌مندی‌ها
- 🔍 Advanced search & filtering — جستجو و فیلتر پیشرفته
- 🔌 Complete REST API — API کامل
- 🧪 Automated tests — تست‌های خودکار
- 🚀 Production deployment — Deploy روی سرور
- 🔐 Production settings — تنظیمات Production

## 🎯 Goal | هدف پروژه

**English:** This project is part of my journey in building real-world Django applications, focusing on backend development, authentication, database design, e-commerce logic, and user interface design.

**فارسی:** این پروژه بخشی از مسیر یادگیری و ساخت پروژه‌های واقعی با Django است و روی Backend، Authentication، طراحی Database، منطق فروشگاه و طراحی رابط کاربری تمرکز دارد.

## 👨‍💻 Author | سازنده

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

⭐ If you find the project useful, give it a star.

⭐ اگر پروژه برایتان مفید بود، خوشحال می‌شوم به Repository Star بدهید.
