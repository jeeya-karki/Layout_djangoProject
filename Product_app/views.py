from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"Home_page.html")

def About_us(request):
    return render(request,"About_us.html")

def services(request):
    return render(request,"services.html")
