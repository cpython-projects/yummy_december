from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import UserRegistrationForm, UserLoginForm


def logout_user(request):
    logout(request)
    return reverse('yummy:home')


# User Registration
class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')


# User Login
class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next') or self.request.POST.get('next') or '/'

