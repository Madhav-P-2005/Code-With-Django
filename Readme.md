# 📘 Introduction to Django — A Complete Beginner’s Guide

A hands-on journey to mastering **Django**, one of the most powerful web frameworks for Python. This repo documents the foundational steps — from setup to app creation — with clean structure, real commands, and detailed explanations.

---

## 🚀 What You'll Learn

- Creating a Django project and app  
- Configuring project settings  
- Defining views and mapping URLs  
- Running the development server  
- Understanding the Django project structure  

---

## 🛠️ Project Setup

### 📁 Step 1 :-  Create a Project Directory

```bash
mkdir Django-Learning && cd Django-Learning
````

---

### 🐍 Step 2 :-  Setup Virtual Environment (Highly Recommended)

```bash
python -m venv MyEnvironment
```

#### ✅ Activate the virtual environment

```bash
.\MyEnvironment\Scripts\Activate.ps1  # For PowerShell on Windows
```

> To deactivate:

```bash
deactivate
```

---

### 📦 Step 3 :-  Install Django

```bash
pip install django
```

---

### ⚙️ Step 4 :-  Start a Django Project

```bash
django-admin startproject myproject .
```

> `.` ensures the project is created in the current folder instead of adding an extra nested directory.

---

### 🧱 Step 5 :-  Create an App

```bash
python manage.py startapp myapp
```

---

### 📌 Step 6 :-  Register the App

Add `'myapp'` to the `INSTALLED_APPS` list inside `myproject/settings.py`.

---

### 🗄️ Step 7 :-  Apply Initial Migrations

Before running the server, apply the default migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

> ⚠️ This step is essential to avoid warnings and errors related to unapplied migrations.

---

### ▶️ Step 8 :-  Run the Development Server

```bash
python manage.py runserver
```

---

## 🧠 Understanding the Project Structure

### 🌐 `myproject/`

Contains the project’s core configuration — settings, URLs, and WSGI/ASGI interfaces.

### 📦 `myapp/`

Contains the application-specific logic — views, models, and templates.

You can create multiple apps in one Django project (e.g., blog, users, store).

---

## 📂 Key Files and Their Purpose

| File / Folder          | Purpose                                                                          |
| ---------------------- | -------------------------------------------------------------------------------- |
| `manage.py`            | Command-line utility to interact with the project (runserver, migrations, etc.). |
| `settings.py`          | Holds configuration settings like database, installed apps, static files, etc.   |
| `urls.py`              | Maps URLs to corresponding views (acts as a request router).                     |
| `views.py`             | Handles request logic and returns responses (HTML, JSON, etc.).                  |
| `models.py`            | Defines your database schema using Django ORM.                                   |
| `admin.py`             | Configures which models are accessible via the admin dashboard.                  |
| `apps.py`              | Holds metadata for your Django app.                                              |
| `tests.py`             | Contains unit tests for validating app functionality.                            |
| `db.sqlite3`           | Lightweight default development database.                                        |
| `wsgi.py`              | Interface for deploying the app using WSGI-compatible servers.                   |
| `asgi.py` *(optional)* | Used for asynchronous applications (e.g., WebSockets).                           |

---

## 📌 Note

This is just the beginning — many more Django features to come including:

* Models and Migrations
* Django Admin Customization
* Templates & Static Files
* Forms & Validations
* Authentication
* Django REST Framework

Stay tuned — this repository will grow with more content, projects, and best practices!

---

## 📚 References

* [Django Official Docs](https://docs.djangoproject.com/en/5.2/)
* [🌐 HttpRequest Docs](https://docs.djangoproject.com/en/5.2/ref/request-response/)
* [🔐 URLconf & Path Parameters](https://docs.djangoproject.com/en/5.2/topics/http/urls/)
* [🧾 Handling Forms and Data](https://docs.djangoproject.com/en/5.2/topics/forms/)

---

Happy Coding 💻✨