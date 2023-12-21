from .django.urls import  path
from .views import vegtable


urlpatterns = [
    path('veg/', vegtable),

]
