from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Nome Completo',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('As senhas não coincidem.')
        return cd['password2']

class PerfilRegistrationForm(forms.ModelForm):
    class Meta:
        model = Perfil
        # Exclui os campos que serão preenchidos manualmente na view
        exclude = ['usuario', 'nome_completo']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ['usuario']
