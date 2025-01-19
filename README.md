﻿# Bynry-Django-Backend-Task

## Overview
This repository contains the backend task for Bynry built with Django. Follow the instructions below to set up the project on your local machine.

## Prerequisites
Ensure you have the following installed on your local machine:
- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sarthakn21/Bynry-Django-Backend-Task.git
   cd Bynry-Django-Backend-Task

2. **Create a virtual environment**
   ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows, use `.venv\Scripts\activate`

3. **Install the required dependencies**
    ```bash
    pip install -r Bynry/requirements.txt
    
4. **Create the media folder inside the Bynry directory**
    ```bash
    mkdir Bynry/media

5. **Apply the database migrations**
    ```bash
    python manage.py makemigrations   # Only if there are changes to the models
    python manage.py migrate
6. **Create a superuser (optional, but recommended for admin access)**
To access the Django admin interface, create a superuser by running the following command:
    ```bash
    python manage.py createsuperuser

7. **Run the development server**
    ```bash
    python manage.py runserver
**Project Structure**

```Directory structure:
└── sarthakn21-bynry-django-backend-task/
    ├── README.md
    ├── requirements.txt
    └── Bynry/
        ├── manage.py
        ├── requirements.txt
        ├── Bynry/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   ├── wsgi.py
        │   └── __pycache__/
        ├── customer_service/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── forms.py
        │   ├── models.py
        │   ├── tests.py
        │   ├── urls.py
        │   ├── views.py
        │   ├── .gitignore
        │   ├── __pycache__/
        │   ├── migrations/
        │   │   ├── 0001_initial.py
        │   │   └── __init__.py
        │   └── templates/
        │       ├── agent_dashboard.html
        │       ├── agent_request_detail.html
        │       ├── index.html
        │       ├── service_request_form.html
        │       └── service_request_list.html
        ├── templates/
        |    ├── layout.html
        |    └── registration/
        |        ├── logged_out.html
        |        ├── login.html
        |        └── register.html
        |
        ├── media/
```


**Bynry/settings.py:** Contains the configuration settings for the Django project.

**Bynry/requirements.txt:** Lists the dependencies required by the project.

**Bynry/customer_service:** Contains the main app for customer service-related functionalities.

**Bynry/media:** Directory to store user-uploaded files.
