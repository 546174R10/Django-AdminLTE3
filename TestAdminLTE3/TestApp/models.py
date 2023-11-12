from django.db import models

# Create your models here.
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class datos(models.Model):
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image=models.ImageField(upload_to='images/images')
    url = URLField(blank=True) 
