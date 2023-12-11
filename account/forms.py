from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


# Create User Login Form
class UserLoginForm(AuthenticationForm):
    """
    User Login Form.
    """
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'Your Username',
                                                                              'class': 'form-control',
                                                                              'id': 'username',
                                                                              'data-rule': 'minlen:4',
                                                                              'data-msg': 'Please enter at least 4 chars'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Your Password',
                                                                                   'class': 'form-control',
                                                                                   'id': 'password',
                                                                                   'data-rule': 'minlen:4',
                                                                                   'data-msg': 'Please enter at least 4 chars'}))

# Create User Registration Form
class UserRegistrationForm(UserCreationForm):
    """
    User Registration Form.
    """
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'Your Username',
                                                                              'class': 'form-control',
                                                                              'id': 'username',
                                                                              'data-rule': 'minlen:4',
                                                                              'data-msg': 'Please enter at least 4 chars'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                            'class': 'form-control',
                                                                            'id': 'email',
                                                                            'data-rule': 'email',
                                                                            'data-msg': 'Please enter a valid email'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Your Password',
                                                                                   'class': 'form-control',
                                                                                   'id': 'password',
                                                                                   'data-rule': 'minlen:4',
                                                                                   'data-msg': 'Please enter at least 4 chars'}))
    password2 = forms.CharField(label='confirm_password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password',
                                                                                                   'class': 'form-control',
                                                                                                   'id': 'confirm_password',
                                                                                                   'data-rule': 'minlen:4',
                                                                                                   'data-msg': 'Please enter at least 4 chars'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
