from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Used to create the form for user registration"""

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class ChangePassForm(UserCreationForm):
    """Used to create the form for users to change their passwords."""
    password1 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('password1', 'password2',)
