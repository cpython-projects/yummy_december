from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from yummy.models import Reservation
from .forms import ReservationEditForm
from django.urls import reverse_lazy, reverse


class ManagerAccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()


class ManagerIndex(LoginRequiredMixin, ManagerAccessMixin, ListView):
    template_name = 'manager_index.html'
    login_url = '/login/'
    model = Reservation
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(is_precessed=False).order_by('date', 'time')


class EditReservation(LoginRequiredMixin, ManagerAccessMixin, UpdateView):
    template_name = 'edit_reservation.html'
    login_url = '/login/'
    model = Reservation
    form_class = ReservationEditForm
    success_url = reverse_lazy('manager:index')