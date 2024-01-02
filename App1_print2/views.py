from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vegtable(request):
    return HttpResponse("This fuction is related to vegetables")


