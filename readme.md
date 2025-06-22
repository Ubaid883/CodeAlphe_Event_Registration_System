# 🎉 Event Registration System API (Django + DRF)
A backend API system built with **Django** and **Django REST Framework (DRF)** that allows users to register for events, and organizers to manage them via an admin panel or secured endpoints.
## ✅ Features
- 🔧 Backend powered by Django & Django REST Framework (DRF)
- 🗃️ Models for Events and Registrations
- 🔗 Registrations linked to both Users and Events
- 🔐 Optional authentication for event organizers
- 📃 RESTful API endpoints for:
  - Listing all events
  - Viewing event details
  - Submitting and managing registrations
- 🛡️ Admin interface to manage users, events, and registrations

    ```bash
    git https://github.com/Ubaid883/CodeAlphe_Event_Registration_System.git
    cd CodeAlpha_Event_Registration_System


##  Create a Virtual Environment

    
    python -m venv myenv
    myenv\Scripts\activate     # On Windows

## Install Requirements

    pip install -r requirements.txt


## 4. Configure Database
Example PostgreSQL config in settings.py:


    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

## Run Migrations & Create Superuser

    python manage.py migrate
    python manage.py createsuperuser

## 6. Run Development Server

    python manage.py runserver


## 🧪 API Endpoints (Sample)
| Method |	Endpoint |	Description |
| -------|-----------|--------------|
|GET     |/event/|	List all events |
|POST|	/register/|	Submit registration for an event
|GET|	/api/registrations/|	View all registrations (admin/user)
|DELETE|	/api/registrations/<int:id>/|	Cancel a specific registration

## 🛠 Admin Panel
- Visit /admin/ to manage:
- Events
- Registrations
- Users (Organizers)

Superusers can be created with:

    python manage.py createsuperuser

## 📚 Tech Stack
- Django
- Django REST Framework
- PostgreSQL (or other supported DBs)
- DRF SimpleJWT (optional)
- Django Admin

