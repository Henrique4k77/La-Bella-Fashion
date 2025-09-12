from django import forms
from django.contrib.auth import get_user_model
from .models import Perfil # Importamos o nosso novo modelo de Perfil

# Importa o modelo de usuário padrão do Django
User = get_user_model()

# Este formulário lida com os campos do modelo de usuário padrão
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# Este formulário lida com os campos do nosso modelo de perfil personalizado
class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefone', 'endereco', 'foto_perfil']