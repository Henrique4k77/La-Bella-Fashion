from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('meus-dados/', views.meus_dados, name='meus_dados'),
    path('editar-dados/', views.editar_dados, name='editar_dados'),
    path('excluir-perfil/', views.excluir_perfil, name='excluir_perfil'),
    path('sair/', views.sair, name='logout'),
]