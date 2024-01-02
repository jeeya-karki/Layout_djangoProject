from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fruit(request):
    return HttpResponse("Apple <br> Orange <br> Grapes <br> Banana")

