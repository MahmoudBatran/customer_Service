from django.urls import path
from .views import deletecustomer

from customers.views import customersIndex, hello_customers,showCustomer,deletecustomer

urlpatterns = [
   
    path("customers",hello_customers),
    path("index", customersIndex,name= "customersindex"),
    path("<customer_id>", showCustomer, name="showcustomer"),
    path("delete/<customer_id>", deletecustomer, name="deletecustomer"),

]
 