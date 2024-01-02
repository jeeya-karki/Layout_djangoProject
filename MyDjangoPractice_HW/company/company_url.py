from django.urls import path
from .views import *

urlpattern=[
    path('hhh/',"home",name="Home"),
     path('ccc/',"contact",name="Contact"),
      path('aaa/',"about",name="About")
]
