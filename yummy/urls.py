from django.urls import path
from .views import main

app_name = 'yummy'

urlpatterns = [
    path('', main, name='home'),
]
