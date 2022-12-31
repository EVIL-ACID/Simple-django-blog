# Simple-django-blog that integrates WYSIWYG ckeditor in the admin panel. <br/>
![djblog](https://user-images.githubusercontent.com/120695832/209859444-f838d65d-180a-4a5f-9d4f-10563ca9adf5.gif)

 <br/>
 <br/>
 
 # Ckeditor integrations 
 
![ckblog](https://user-images.githubusercontent.com/120695832/209859507-adcf0500-f006-438e-9301-6e4baf09f5c7.PNG)


# Set up
<br/>

## You will need to install dependencies for this to work.

> pip install -r requirements.txt


## CD to the blog directory and run the following migrations 
```
cd blog

python manage.py makemigrations

python manage.py migrate
```

## Create a super user to be able to create blog posts.


```
python manage.py createsuperuser
```

## Run the server

```
python manage.py runserver
```
