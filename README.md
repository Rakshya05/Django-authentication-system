# Django Authentication system
This project is based on my knowlwedge in Django.This project is based on simple django application where login is done via email and password.To show how to run this application in local server run this step:
## Steps
Install virtual environment from terminal
```bash
pip install virtualenv
```
Created virtual environment named venv

```bash
python3 -m venv venv
```
Activate the virtual environment venv
```bash
source django/bin/activate
 ```
Install necessary requirements
```bash
pip install django
 ```
To create new migrations based on the changes that have made to in Django models.
```bash
python manage.py  makemigrations
 ```
To execute the migrations and update the database schema accordingly
```bash
python manage.py migrate
 ```
To test your web application locally during the development phase.
```bash
python manage.py runserver
