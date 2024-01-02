from django.shortcuts import render
from .views import *
# Create your views here.
def Home(request):
    return render(request,'Emp/home.html')

def contact(request):
    return render(request,'Emp/contact.html')

def user(request):
    return  render(request,'Emp/user.html')