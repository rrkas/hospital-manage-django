# Hospital Management System

## Features
1. organization
   - managing users, patients, doctors
2. users (staffs)
   - register
   - login
3. staffs (created when users register)
   - list
   - view
   - update
   - archive
4. patients
   - Create
   - list
   - View
   - update
   - archive
5. doctors
6. equipments
7. news_updates

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
