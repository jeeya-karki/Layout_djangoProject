from django.urls import path
from .views import *



urlpatterns = [
    path('home/', Home , name="home"),
    path('about/', About_us , name="about_us"),
    path('services/', services , name="services"),

]
