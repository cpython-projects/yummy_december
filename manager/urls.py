from django.urls import path
from .views import ManagerIndex

app_name = 'manager'

urlpatterns = [
    path('', ManagerIndex.as_view(), name='index'),
]