# 📘 Django To-Do App — A Beginner to Intermediate Journey

Welcome to my Django learning journey — documented, structured, and evolving in real-time. This repo begins with setting up Django from scratch and progresses into building a **full-featured To-Do App** using Django’s powerful capabilities.

---

## 🚀 What You’ll Learn

This repository covers both foundational and intermediate-level Django development concepts :-  

### 🔰 Basics

* Setting up a Django Project & App
* Virtual Environment Configuration
* Understanding Django Project Structure
* URL Routing and Views

### 🧱 Intermediate Features

* CRUD Operations with Django ORM
* SQLite3 Integration
* User Authentication (Login/Logout)
* Middleware Implementation
* Real-Time Updates with Django Channels
* API Endpoints: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
* Pagination & Query Parameters
* Postman API Testing and Collection Export

---

## 💡 Project Outcome

A fully functional, tested **To-Do Application**:

* Create, read, update, delete tasks
* Filter tasks using parameters
* Authenticate users for personalized task lists
* Real-time updates when a task is added or modified

🔗 Postman Collection included → [Click to View Collection](https://documenter.getpostman.com/view/38375474/2sB3B7NZL4#intro)

---

## 🛠️ Project Setup Instructions

### 1. Create Project Directory

```bash
mkdir Django-Learning && cd Django-Learning
```

### 2. Setup Virtual Environment

```bash
python -m venv MyEnvironment
.\MyEnvironment\Scripts\Activate.ps1  # PowerShell (Windows)
```

> To deactivate:
> `deactivate`

### 3. Install Django

```bash
pip install django
```

### 4. Start Project

```bash
django-admin startproject myproject .
```

### 5. Create App

```bash
python manage.py startapp myapp
```

### 6. Register App in `settings.py`

```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

### 7. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Run Server

```bash
python manage.py runserver
```

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

## 🧪 API Testing (Postman)

All API routes were tested using Postman. A structured collection with example requests is available in this repo.

> 📁 \_Includes over 30+ structured requests for:
>
> * Auth
> * CRUD
> * Pagination
> * Middleware\_

---

## 🏁 Certificates Earned

🏅 4 individual course certifications
🏅 1 full learning path certificate for **"Introduction to Django for Back-End Development"** by CodeSignal

---

## 💻 What’s Next?

📋 **Mastering Django Admin Panel**
🔍 Deep diving into **Django REST Framework (DRF)**
🚀 Learning deployment strategies (Heroku, Railway, etc.)
🏗️ Building **real-world production-ready projects**
🛠️ Implementing best practices for scalability and security

---

## 📚 References

* [Django Official Documentation](https://docs.djangoproject.com/en/5.2/)
* [Postman Learning Center](https://learning.postman.com/)
* [Django ORM Guide](https://docs.djangoproject.com/en/5.2/topics/db/models/)
* [Django Channels Docs](https://channels.readthedocs.io/en/latest/)

---

## 🙌 Acknowledgements

Thanks to **CodeSignal** for a structured, beginner-friendly path.

---

### 🌟 Star this repo if it helped you — and feel free to fork, learn, and contribute.