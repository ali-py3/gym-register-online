from django import forms
from .models import User, Tuition
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20, min_length=5)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'mobile_number', 'address', 'natioral_code',
                  'date_birth', 'password1', 'password2']
