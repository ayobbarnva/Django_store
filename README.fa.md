<div dir="rtl">

# 🛒 Django Store

**یک فروشگاه اینترنتی مدرن، Responsive و دو زبانه ساخته‌شده با Django**

</div>

🇬🇧 [English](README.md) | 🇮🇷 **فارسی**

## ✨ درباره پروژه

**Django Store** یک پروژه فروشگاه اینترنتی Full-Stack است که روی مدیریت کاربران، احراز هویت، محصولات، دسته‌بندی‌ها، پروفایل و منطق سبد خرید تمرکز دارد.

## 🚀 امکانات

- 🛍️ نمایش محصولات
- 🗂️ دسته‌بندی محصولات
- 🔎 صفحه جزئیات محصول
- 💰 قیمت و تخفیف
- 📦 مدیریت موجودی
- 🛒 سبد خرید
- ➕ افزایش تعداد
- ➖ کاهش تعداد
- ❌ حذف محصول
- 👤 سیستم کاربری اختصاصی
- 🔐 ثبت‌نام و ورود
- 🖼️ تصویر پروفایل
- ✏️ ویرایش پروفایل
- 📱 طراحی Responsive
- 🌐 پشتیبانی فارسی و انگلیسی
- 🌓 حالت روشن و تاریک
- ⚙️ Django Admin

## 🧰 تکنولوژی‌ها

| تکنولوژی | کاربرد |
|---|---|
| 🐍 Python | Backend |
| 🎯 Django 6.1 | Web Framework |
| 🔌 Django REST Framework | توسعه API |
| 🖼️ Pillow | مدیریت تصاویر |
| 🌐 HTML | قالب‌ها |
| 🎨 CSS | رابط کاربری |
| ⚡ JavaScript | تعاملات Frontend |
| 🗄️ SQLite | پایگاه داده توسعه |

## 📁 ساختار پروژه

```text
Django_store/
├── accouants/       # کاربران و احراز هویت
├── app/             # محصولات و دسته‌بندی‌ها
├── cart/            # سبد خرید
├── profile/         # پروفایل کاربران
├── project_django/  # تنظیمات اصلی Django
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ نصب و اجرا

```bash
git clone https://github.com/ayobbarnva/Django_store.git
cd Django_store
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

در Windows:

```powershell
.venv\Scripts\activate
```

## 🔐 متغیرهای محیطی

اطلاعات حساس مانند `SECRET_KEY` را داخل `.env` نگه دارید و آن را وارد Repository عمومی نکنید.

## 🗄️ Migration

این پروژه چند Django App دارد. برای Migration هر App می‌توانید جداگانه اجرا کنید:

```bash
python manage.py makemigrations accouants
python manage.py makemigrations app
python manage.py makemigrations cart
python manage.py makemigrations profile
```

یا همه Appها را یکجا بررسی کنید:

```bash
python manage.py makemigrations
```

سپس:

```bash
python manage.py migrate
```

## 👤 ساخت ادمین

```bash
python manage.py createsuperuser
```

## ▶️ اجرای پروژه

```bash
python manage.py runserver
```

سپس:

```text
http://127.0.0.1:8000/
```

## 🛒 سبد خرید

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

- 💳 درگاه پرداخت
- 📋 سیستم سفارش و Checkout
- 📦 تاریخچه سفارش‌ها
- ❤️ Wishlist
- 🔍 جستجو و فیلتر پیشرفته
- 🔌 API کامل
- 🧪 تست‌های خودکار
- 🚀 Deploy روی سرور
- 🔐 تنظیمات Production

## 👨‍💻 سازنده

**Ayoob Barnva** — [@ayobbarnva](https://github.com/ayobbarnva)

⭐ اگر پروژه برایتان مفید بود، خوشحال می‌شوم به Repository Star بدهید.
