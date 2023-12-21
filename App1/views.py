from django.shortcuts import render

# Create your views here.
def fruit(request):
    return render("Apple <br> Orange <br> Grapes <br> Banana")

