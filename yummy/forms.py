from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    name = forms.CharField(label='name',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Your Name',
                               'data-rule': 'minlen:4',
                               'data-msg': 'Please enter at least 4 chars'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                           'class': 'form-control',
                                                                           'id': 'email',
                                                                           'data-rule': 'email',
                                                                           'data-msg': 'Please enter a valid email'}))
    phone = forms.CharField(label='phone', widget=forms.TextInput(attrs={'placeholder': 'Your Phone',
                                                                         'class': 'form-control',
                                                                         'id': 'phone',
                                                                         'data-rule': 'minlen:4',
                                                                         'data-msg': 'Please enter a valid phone: 0xxxxxxxxx'}))
    date = forms.DateField(label='date', widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD',
                                                                       'class': 'form-control',
                                                                       'id': 'date',
                                                                       'data-rule': 'minlen:4',
                                                                       'data-msg': 'Please enter at least 4 chars'}))
    time = forms.TimeField(label='time', widget=forms.TimeInput(attrs={'placeholder': 'HH:MM',
                                                                       'class': 'form-control',
                                                                       'id': 'time',
                                                                       'data-rule': 'minlen:2',
                                                                       'data-msg': 'Please enter at least 2 chars'}))
    people = forms.IntegerField(label='people', widget=forms.NumberInput(attrs={'placeholder': '# of people',
                                                                                'class': 'form-control',
                                                                                'id': 'people',
                                                                                'data-rule': 'minlen:1'}))
    message = forms.CharField(label='message', widget=forms.Textarea(attrs={'placeholder': 'Message',
                                                                            'class': 'form-control',
                                                                            'rows': '5'}))

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'people', 'message')