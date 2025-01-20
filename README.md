# Bynry-Django-Backend-Task

## Overview

Django application to provide consumer services for gas utilities. The application
would allow customers to submit service requests online, track the status of their requests,
and view their account information.
The application would also provide customer support representatives with a tool to manage
requests and provide support to customers. The project allows customers to request services and provides two types of user roles: **Customer** and **Admin**.

### Key Features:
- **Customer Interface**: Customers can log in to the system, view their dashboard, and submit new service requests. They can also track the status of their ongoing requests.
- **Admin Interface**: Admin users can log in to access the **Admin Dashboard**, where they can:
  - View all service requests submitted by customers.
  - Change the status of service requests (e.g., open, in-progress, resolved).
  - Edit service requests as needed.
- **Authentication**: Users can register, log in, and log out to securely manage their service requests. Customers are directed to the customer page upon login, while admins are redirected to the admin dashboard.
- **File Upload**: Users can upload files related to their service requests using the Pillow library.
- **Media Management**: All uploaded files are stored in the `media` folder for easy access and retrieval.
- **Database Management**: The project uses SQLite for its database, making it easy to set up and run locally for testing and development purposes.
- **Django Admin Panel**: Admin users can also manage the system through Django’s built-in admin panel after creating a superuser.

This project was built with the goal of providing an efficient and user-friendly solution to handle customer service requests, ensuring that admins have full control over the service requests and customers can easily interact with the system.



![Screenshot 2025-01-19 224222](https://github.com/user-attachments/assets/da8a62cd-ef61-4b0b-bb95-f3d161bbe80a)
![Screenshot 2025-01-19 224705](https://github.com/user-attachments/assets/a21029f6-66e1-494c-98d6-91c68eb3a56f)
![Screenshot 2025-01-19 224244](https://github.com/user-attachments/assets/fca7ab0c-b5ca-4e50-9118-91a98b5e3bc1)
![Screenshot 2025-01-19 224715](https://github.com/user-attachments/assets/694901e0-e8ea-498c-b3c1-a88ac4023c18)
![Screenshot 2025-01-20 100033](https://github.com/user-attachments/assets/d7a07373-70c3-494b-9097-52f23f28f214)
![Screenshot 2025-01-20 100200](https://github.com/user-attachments/assets/e5cfe01d-9071-4fc7-93dd-94e76e4c1fa3)

![Screenshot 2025-01-19 225832](https://github.com/user-attachments/assets/f22642fa-748b-47db-8bda-03724057dfcb)

![Screenshot 2025-01-20 093704](https://github.com/user-attachments/assets/70ae971e-6fa0-4157-946e-2a074a2ae605)
![Screenshot 2025-01-20 093637](https://github.com/user-attachments/assets/d3a105eb-7c5c-4e88-b414-f83b88631023)
![Screenshot 2025-01-20 093644](https://github.com/user-attachments/assets/7583a1c7-ed24-4ebc-98ba-1e3a7a94c3ff)


## Prerequisites
This repository contains the backend task for Bynry built with Django. Follow the instructions below to set up the project on your local machine.
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
    ├── .venv
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
