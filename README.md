# Simple-django-blog that integrates WYSIWYG ckeditor in the admin panel. <br/>
![djblog](https://user-images.githubusercontent.com/120695832/209859444-f838d65d-180a-4a5f-9d4f-10563ca9adf5.gif)

 <br/>
 <br/>
 
 # Ckeditor integrations 
 
![ckblog](https://user-images.githubusercontent.com/120695832/209859507-adcf0500-f006-438e-9301-6e4baf09f5c7.PNG)


# Set up
<br/>

```
CD into the projects directory
pipenv shell
cd blog
```

## Installing all dependencies.

```
pip install -r requirements.txt
```
## Migrations 
```
 python manage.py migrate
 python manage.py makemigrations blogapp
 python manage.py migrate blogapp
```
## Create a super user to be able to create blog posts.
```
 python manage.py createsuperuser
```
## Run server

```
 manage.py ruserver
```
