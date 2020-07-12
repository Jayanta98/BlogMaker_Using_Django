from django.shortcuts import render
from datetime import datetime
from JGapp.models import Customer
# Create your views here.
def index(request):
    return render(request,'index.html')



#def about(request):
    #return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        cust_name=request.POST.get('name1')
        cust_email=request.POST.get('mail')
        cust_password=request.POST.get('myp')
        
        x= Customer(name=cust_name,email=cust_email,password=cust_password)
        x.save()

    return render(request,'contact.html')
