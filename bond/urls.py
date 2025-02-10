from django.urls import path, include
from bond import urls 
from .views import * 



urlpatterns = [
   
    path('',homeView),
]
