from django.urls import path
from .views import IndexPage

app_name = 'yummy'

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
]
