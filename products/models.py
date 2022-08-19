from platform import mac_ver
from pyexpat import model
from django.db import models

# Create your models here.
class product (models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField(default=200)
    descriptions = models.CharField(null=True, max_length=100)
    img= models.CharField(null= True, max_length=2000)
    no_of_items= models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True, null=True)
    edited_at=models.DateTimeField(auto_now_add=True, null=True)
    