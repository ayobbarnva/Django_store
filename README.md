# 🛒 فروشگاه Django

> یک فروشگاه اینترنتی Responsive و دو زبانه که با Django ساخته شده و به‌عنوان یک پروژه عملی و نمونه‌کار توسعه داده شده است.

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-11.1.0-3776AB?style=for-the-badge)

---

## ✨ درباره پروژه

**Django Store** یک پروژه فروشگاه اینترنتی Full-Stack ساخته‌شده با Django است.

تمرکز پروژه روی پیاده‌سازی مفاهیم واقعی توسعه وب مانند مدیریت کاربران، محصولات، دسته‌بندی‌ها، پروفایل، احراز هویت و منطق سبد خرید است.

این پروژه به‌عنوان یک پروژه آموزشی و نمونه‌کار ساخته شده و در آینده می‌توان امکاناتی مانند سفارش، Checkout، پرداخت و API را به آن اضافه کرد.

## 🚀 امکانات

- 🛍️ نمایش محصولات
- 🗂️ دسته‌بندی محصولات
- 🔎 صفحه جزئیات محصول
- 💰 قیمت و تخفیف محصولات
- 📦 مدیریت موجودی
- 🛒 سبد خرید
- ➕ افزایش تعداد محصول
- ➖ کاهش تعداد محصول
- ❌ حذف محصول از سبد خرید
- 👤 سیستم کاربری اختصاصی
- 🔐 ثبت‌نام و ورود کاربران
- 🖼️ تصویر پروفایل
- ✏️ ویرایش پروفایل
- 📱 طراحی Responsive
- 🌐 پشتیبانی فارسی و انگلیسی
- 🌓 حالت روشن و تاریک
- ⚙️ مدیریت محصولات و دسته‌بندی‌ها از طریق Django Admin

## 🧰 تکنولوژی‌ها

| تکنولوژی | کاربرد |
|---|---|
| 🐍 Python | Backend |
| 🎯 Django 6.1 | Web Framework |
| 🔌 Django REST Framework | توسعه API |
| 🖼️ Pillow | مدیریت تصاویر |
| 🌐 HTML | قالب‌ها |
| 🎨 CSS | طراحی رابط کاربری |
| ⚡ JavaScript | تعاملات Frontend |
| 🗄️ SQLite | پایگاه داده توسعه |

## 📁 ساختار پروژه

```text
Django_store/
├── accouants/          # کاربران و احراز هویت
├── app/                # محصولات و دسته‌بندی‌ها
├── cart/               # سبد خرید
├── profile/            # پروفایل کاربران
├── project_django/     # تنظیمات اصلی Django
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ نصب و اجرا

### 1. دریافت پروژه

```bash
git clone https://github.com/ayobbarnva/Django_store.git
cd Django_store
```

### 2. ساخت محیط مجازی

```bash
python -m venv .venv
source .venv/bin/activate
```

در Windows:

```powershell
.venv\Scripts\activate
```

### 3. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

### 4. تنظیم متغیرهای محیطی

یک فایل `.env` بسازید و اطلاعات حساس مانند `SECRET_KEY` را داخل آن قرار دهید.

> ⚠️ کلید واقعی Django را داخل Repository عمومی قرار ندهید.

## 🗄️ Migration

این پروژه از چند Django App تشکیل شده است. در صورت تغییر Modelهای هر App می‌توانید Migration همان App را جداگانه ایجاد کنید:

```bash
python manage.py makemigrations accouants
python manage.py makemigrations app
python manage.py makemigrations cart
python manage.py makemigrations profile
```

یا برای بررسی همه Appها به‌صورت یکجا:

```bash
python manage.py makemigrations
```

سپس Migrationها را روی Database اعمال کنید:

```bash
python manage.py migrate
```

## 👤 ساخت کاربر ادمین

```bash
python manage.py createsuperuser
```

## ▶️ اجرای پروژه

```bash
python manage.py runserver
```

سپس وارد شوید:

```text
http://127.0.0.1:8000/
```

## 🛒 روند سبد خرید

```text
Product
   ↓
Add to Cart
   ↓
Cart
   ├── ➕ افزایش تعداد
   ├── ➖ کاهش تعداد
   └── ❌ حذف محصول
```

## 🔮 امکانات آینده

- 💳 اتصال درگاه پرداخت
- 📋 سیستم Order و Checkout
- 📦 تاریخچه سفارش‌ها
- ❤️ Wishlist
- 🔍 جستجو و فیلتر پیشرفته محصولات
- 🔌 API کامل
- 🧪 تست‌های خودکار
- 🚀 Deploy روی سرور
- 🔐 تنظیمات Production

## 🎯 هدف پروژه

این پروژه بخشی از مسیر یادگیری و ساخت پروژه‌های واقعی با Django است و روی Backend، Authentication، طراحی Database، منطق فروشگاه و طراحی رابط کاربری تمرکز دارد.

## 👨‍💻 سازنده

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

⭐ اگر پروژه برایتان مفید بود، خوشحال می‌شوم به Repository Star بدهید.
