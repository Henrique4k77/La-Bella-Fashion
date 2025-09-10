from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('usuario/', include('usuario.urls')),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar'),
    
    # Adicione estas URLs para as páginas de perfil
    path('meus_dados/', views.meus_dados, name='meus_dados'),
    path('meus_dados/editar/', views.editar_dados, name='editar_dados'),
    path('meus_dados/excluir/', views.excluir_perfil, name='excluir_perfil'),
]