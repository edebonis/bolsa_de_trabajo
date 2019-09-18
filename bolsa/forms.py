from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bolsa.models import Profile


class SignUpForm(UserCreationForm):
    first_name = Profile.first_name
    last_name = Profile.last_name
    email = Profile.email
    telefono = Profile.telefono
    # is_staff = Profile.is_staff
    # birth_date = Profile.birth_date

    class Meta:
        model = Profile
        fields = {'username':'nombre_de_usuario',
                  'first_name': 'primer_nombre',
                  'last_name':'apellido',
                  'email':'email',
                  'password1':'password1',
                  'password2':'password2',
                  'telefono':'telefono'}

