from django.db import models
from django.shortcuts import get_object_or_404
from platform import mac_ver
from pyexpat import model
from calendar import c
from django.shortcuts import reverse 

# Create your models here.
class customer(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='customers/images/', null= True)
    age= models.IntegerField(default=30)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    @classmethod 
    def get_All_customers(cls):
        return cls.objects.all()
    @classmethod 
    def  show_customer(cls,id):
        return get_object_or_404(cls, pk=id)

    def get_image_url(self):
        return f"/media/{self.image}"
    
    def get_customer_url(self):
        return reverse("showcustomer", args=[self.id])



    def get_delete_url(self):
        return reverse("deletecustomer", args=[self.id])

    @classmethod
    def get_all_url(cls):
         return reverse("customersindex")
