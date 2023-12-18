from django.urls import path
from .views import ManagerIndex, EditReservation

app_name = 'manager'


urlpatterns = [
    path('', ManagerIndex.as_view(), name='index'),
    path('reservation/<int:pk>/', EditReservation.as_view(), name='edit_reservation'),
]