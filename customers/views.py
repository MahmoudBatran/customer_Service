from django.shortcuts import render
from django.http import HttpResponseRedirect
from customers.models import customer


from .models import customer


def hello_customers(request):
    return render(request,'customers/helloworld.html')


def customersIndex(request):
    allcustomers= customer.get_All_customers()
    context= {"customers":allcustomers}
    return render(request,"customers/index.html",context) 

def showCustomer(request, customer_id):
    print(f'customer value is {customer_id}')
    Customer = customer.show_customer(customer_id)
    context  ={"customer": Customer}
    return render(request,"customers/show.html",context)


def deletecustomer(request,customer_id  ):
    delete_customer= customer.show_customer(customer_id)
    url= customer.get_all_url()
    delete_customer.delete()
    return HttpResponseRedirect(url)



    