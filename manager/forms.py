from django import forms
from yummy.models import Reservation


class ReservationEditForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('is_precessed', 'name', 'date', 'time', 'people')

