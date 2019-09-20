from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bolsa.models import Profile, Oportunidad


class SignUpForm(UserCreationForm):
    first_name = Profile.first_name
    last_name = Profile.last_name
    email = Profile.email
    telefono = Profile.telefono

    class Meta:
        model = Profile
        fields = {'username':'nombre_de_usuario',
                  'first_name': 'primer_nombre',
                  'last_name':'apellido',
                  'email':'email',
                  'password1':'password1',
                  'password2':'password2',
                  'telefono':'telefono'}


class NuevaOportuindad(forms.ModelForm):
    class Meta:
        model = Oportunidad
        classmethod = 'POST'
        fields = [
            'user',
            'descripcion',
            'titulo',
            'tipo',
            'visible'
        ]
        labels = {
            'user':'Usuario',
            'descripcion':'Descripción',
            'titulo':'Título',
            'tipo':'Tipo',
            'visible':'Visible'
        }

        def __init__(self, *args, **kwargs):
            super(NuevaOportuindad, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
