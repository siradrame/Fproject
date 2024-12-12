# Fproject

### INF601 - Advanced Programming in Python
### Sira  Drame 
### Mini Project 4

# Django Web Application

## Description
This application allows users to register, log in, and manage their tasks by creating, editing, and deleting them. 

### Dependencies

```
pip install  -r requirements.txt
```


# How  should we run the server
#python manage.py runserver


### Executing program

```
python manage.py runserver
```

### Create the database migrations

```
python manage.py makemigrations
```

## Apply the migrations to the database

```
python manage.py migrate

```

## Create a superuser

```
python manage.py createsuperuser

```

Once the superuser is created, you can log in to the Django admin interface at http://127.0.0.1:8000/taskmanager/ using the credentials you created.
In this case here are the login information of the superuser I created :

Username: sira
Password: changeme


## Authors

Contributors names and contact info

ex. Sira Drame   

## Acknowledgments

Inspiration, code snippets, etc.
* [Django](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
* [ChatGPT](https://chatgpt.com/c/675ae95a-1a4c-800f-b548-efe3f11712bd)