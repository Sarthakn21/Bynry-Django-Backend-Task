# Bynry-Django-Backend-Task

## Overview

This is a Django-based backend project for **Bynry**, a customer service management system. The project allows customers to request services and provides two types of user roles: **Customer** and **Admin**.

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
![Screenshot 2025-01-19 224803](https://github.com/user-attachments/assets/5010e93f-84c8-4a96-bb8f-4a53ed86aa06)
![Screenshot 2025-01-19 225208](https://github.com/user-attachments/assets/4c09cd2f-0739-4e49-8580-3ace465e274f)
![Screenshot 2025-01-19 225653](https://github.com/user-attachments/assets/039192dc-f619-4c8a-b20e-c40d8bd26217)
![Screenshot 2025-01-19 225832](https://github.com/user-attachments/assets/f22642fa-748b-47db-8bda-03724057dfcb)
![Screenshot 2025-01-19 230107](https://github.com/user-attachments/assets/383a181e-68e7-4559-9cbf-36da546d6adb)
![Screenshot 2025-01-19 230117](https://github.com/user-attachments/assets/f8359254-7344-465f-a20b-b8dc9b7c53aa)
![Screenshot 2025-01-19 230127](https://github.com/user-attachments/assets/d0920893-9e40-4791-9aa4-f8874f05f162)
![Screenshot 2025-01-20 000655](https://github.com/user-attachments/assets/86fc6a05-28c3-4a56-8fc5-92426573dc28)


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
