# [Django Argon2 PRO](https://appseed.us/product/argon-dashboard2-pro/django/)

**Django** starter styled with **[Argon2 Design PRO](https://appseed.us/product/argon-dashboard2-pro/django/)**, a premium `Bootstrap 5` KIT from [Creative-Tim](https://bit.ly/3fKQZaL)
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

> **NOTE**: This product `requires a License` in order to access the theme. During the purchase, a `GitHub Access TOKEN` is provided. 

- 🛒 [Django Argon2 PRO](https://appseed.us/product/material-dashboard2-pro/django/) - `Product page` (contains payment links)
- 👉 [Django Argon2 PRO](https://django-argon-dash2-pro.onrender.com/) - `LIVE Demo` on Render
- 🚀 [Support](https://appseed.us/support/) via `Email` & `Discord`

<br />

## Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Argon2](https://github.com/app-generator/django-admin-argon2-pro) - `PRO Version`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Docker`
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

![Argon Dashboard 2 PRO - Charts Page (Premium Bootstrap 5 Design)](https://github.com/app-generator/flask-argon-dashboard2-pro/assets/51070104/168056b7-0886-44ca-8bda-0ae8e76d9076)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-argon-dashboard2-pro.git
$ cd django-argon-dashboard2-pro
```

<br />

> Export `GITHUB_TOKEN` in the environment. The value is provided by AppSeed during purchase. 

This is required because the project has a private REPO dependency: `github.com/app-generator/priv-django-admin-material-pro`

```bash
$ export GITHUB_TOKEN='TOKEN_HERE'  # for Linux, Mac
$ set GITHUB_TOKEN='TOKEN_HERE'     # Windows CMD
$ $env:GITHUB_TOKEN = 'TOKEN_HERE'  # Windows powerShell 
```

<br />

> 👉 Install modules via `VENV`.


```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Edit the `.env` using the template `.env.sample`. 

```env

# True for development, False for production
DEBUG=True

```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Screenshots

![Argon Dashboard 2 PRO - Automotive (Premium Bootstrap 5 Design).](https://user-images.githubusercontent.com/51070104/211158013-fea76b79-bb54-4066-a617-5ec3b4b6ec42.jpg)

<br />

> [Django Argon2 PRO](https://appseed.us/product/argon-dashboard2-pro/django/) - `Charts` Page

![Argon Dashboard 2 PRO - Charts (Premium Bootstrap 5 Design).](https://user-images.githubusercontent.com/51070104/211158055-f29b86dd-0119-433c-af02-5bb41c041049.jpg)

<br />

> [Django Argon2 PRO](https://appseed.us/product/argon-dashboard2-pro/django/) - `eCommerce` Product Page

![Argon Dashboard 2 PRO - eCommerce (Premium Bootstrap 5 Design).](https://user-images.githubusercontent.com/51070104/211158098-afc2b3a6-0c2e-47ea-80d1-c26db0e80da1.jpg)

<br />

---
[Django Argon2 PRO](https://appseed.us/product/argon-dashboard2-pro/django/) - **Django** starter provided by **[AppSeed](https://appseed.us/)**
