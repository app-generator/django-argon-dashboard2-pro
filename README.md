# [Django Argon PRO](https://github.com/app-generator/django-argon-dashboard-pro) `Starter`

**Django** starter styled with **Argon Design PRO**, a premium `Bootstrap 5` KIT from [Creative-Tim](https://bit.ly/3fKQZaL)
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

> **NOTE**: This product `requires a License` in order to access the theme. During the purchase, a `GitHub Access TOKEN` is provided. 

- 👉 [Django Argon PRO](https://django-argon-dashboard-pro.onrender.com) - `LIVE Demo` on Render
- 🚀 [Support](https://appseed.us/support/) via `Email` & `Discord`

<br />

## Purchase Product via `GUMROAD`

- 🛒 `Personal License`: **[PAY - $49](https://appseed.gumroad.com/l/django-argon-pro)** (payment link)
  - Usage [terms](https://github.com/app-generator/license-personal): `Support & Updates: 6mo`
  
- 🛒 `StartUp License`: **[PAY - $99](https://appseed.gumroad.com/l/django-argon-pro-startup)** (payment link)
  - Usage [terms](https://github.com/app-generator/license-startup): `Support & Updates: 12mo`
  
- 🛒 `Company License`: **[PAY - $199](https://appseed.gumroad.com/l/django-argon-pro-company)** (payment link)
  - Usage [terms](https://github.com/app-generator/license-personal): `Support & Updates: Lifetime`, **SaaS** products allowed
  
<br />

## Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Material](https://github.com/app-generator/django-admin-material-pro) - `PRO Version`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Deployment-Ready` for Render 

<br />

![Material Dashboard BS5 - Modern Dashboard design by Creative-Tim.](https://user-images.githubusercontent.com/51070104/209104783-22f04139-8919-457c-b21d-7383d57f07b1.png)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-argon-dashboard-pro.git
$ cd django-argon-dashboard-pro
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

@ToDo

<br />

---
[Django Argon PRO](https://github.com/app-generator/django-argon-dashboard-pro) - Minimal **Django** starter provided by **[AppSeed](https://appseed.us/)**