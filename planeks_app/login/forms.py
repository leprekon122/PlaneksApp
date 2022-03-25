from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
