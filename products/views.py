from http.client import HTTPResponse
import imp
from itertools import product
from multiprocessing import context
import re
from django.shortcuts import render
from django.http import HttpResponse
import json

products=[
{"id":1,"name":"Music Player", "price":1000, "img":"p1.png","description":"This Music Player Device",
"number_of_items":1},

{"id":2,"name":"Mobile", "price":5000, "img":"p2.png","description":"This Smarts Mobile Phone",
"number_of_items":10},

{"id":3, "name":"Camera", "price":6000, "img":"p3.png","description":"This Camera Digital Device",
"number_of_items":100},

{"id":4, "name":"Pepsi Drinks", "price":7000, "img":"p4.png","description":"this is Pepsi souda Drinks",
"number_of_items":1000}
        ]


def hello_product(request):
    return HttpResponse('<h1>Hello</h1>')

def welcome(request):
    return HttpResponse("<h1 style='color:red'>welcome</h1>")
def hello(request,name):
    return HttpResponse(f"<h1 style='color:red'>hello:{name}</h1>")

def helloworld(request):
    # return HttpResponse("<h1>hello</h1>")
    return render(request,"Products/helloworld.html")

def productstestview(request):
     
        context= {"allproducts":products}
        return render(request, "products/productstesttemp.html",context)

def productdetails(request, product_id):
        myproduct= {}
        for p in products :
            if str(p["id"])==product_id:
                myproduct=p
                break
        #myproduct= json.dumps(myproduct )
        #return HttpResponse(myproduct)
        context={"product":myproduct}
        return render(request,"products/productdetails.html",context )