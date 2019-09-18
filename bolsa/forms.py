from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bolsa.models import Profile


class SignUpForm(UserCreationForm):
    first_name = Profile.first_name
    last_name = Profile.last_name
    email = Profile.email
    is_staff = Profile.is_staff
    # birth_date = Profile.birth_date

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff')

