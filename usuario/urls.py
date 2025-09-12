from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='usuario_login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('meus-dados/', views.meus_dados, name='meus_dados'),
    path('editar-dados/', views.editar_dados, name='editar_dados'), # Adicione esta linha
    path('excluir-perfil/', views.excluir_perfil, name='excluir_perfil'), # Adicione esta linha
    path('sair/', views.sair, name='logout'),
]