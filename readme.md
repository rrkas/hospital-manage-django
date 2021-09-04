# Hospital Management System

## Features
1. organization
   - managing users, patients, doctors
2. users (staffs)
   - register users
   - login users
   - staff list screen
   - staff detail screen
3. patients
   - Create patient
   - View patient
4. doctors
5. equipments
6. news_updates

## Setup
Environment:
- `virtualenv venv`  
- `venv\Scripts\activate`

Commands:
- `django-admin startproject hospital_manage`
- `python manage.py startapp patients`
- `python manage.py createsuperuser`
- `python manage.py collectstatic`
- `python manage.py shell`

Running the server: `python manage.py runserver 127.0.0.1:8080`
