from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='usuario_login'),
    path('cadastrar/', views.cadastrar, name='usuario_cadastrar'), # Certifique-se de que esta linha existe
]