
from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PerfilRegistrationForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome_completo']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome_completo', 'telefone', 'endereco', 'foto_perfil']
