
from itertools import product
from django.urls import path
from products.views import  hello_product
from products.views import welcome, hello, helloworld, productstestview, productdetails
urlpatterns = [
    path('hello', hello_product,name="hello"),
    path('welcome',welcome,name="welcome"),
    path('hello/<name>', hello,name="helloname"),
    path("hiworld",helloworld,name="hiworld"),
    path("productstest",productstestview,name="productstest"),
    path("productdetails/<product_id>", productdetails, name="productdetails")]
