from django.urls import path
from .views import *

urlpatterns = [
   path("home/", Home ,name="home"),
   path("contact", contact, name="contact"),
   path("user", user, name="user")
]