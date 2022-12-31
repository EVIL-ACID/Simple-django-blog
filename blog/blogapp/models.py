from django.db import models

# Create your models here.
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.


class blogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    content = RichTextUploadingField()
    description = RichTextUploadingField(default="Description...")

    def __str__(self) -> str:
        return self.title
