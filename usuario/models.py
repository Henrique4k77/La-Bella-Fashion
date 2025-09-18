from django.db import models
from django.contrib.auth.models import User # Importamos o modelo de usuário padrão do Django

class Perfil(models.Model):
    """
    Modelo para armazenar informações adicionais do usuário.
    Cada usuário terá um único perfil associado.
    """
    # Cria uma relação One-to-One com o modelo de usuário padrão
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Campo para o nome completo do usuário
    nome_completo = models.CharField(max_length=100, blank=True, null=True)

    # Campo para o telefone do usuário
    telefone = models.CharField(max_length=20, blank=True, null=True)
    
    # Campo para o endereço completo do usuário
    endereco = models.CharField(max_length=255, blank=True, null=True)
    
    # Novo campo para a foto de perfil
    # A foto será salva na pasta 'media/fotos_perfil'
    foto_perfil = models.ImageField(upload_to='fotos_perfil', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}' 