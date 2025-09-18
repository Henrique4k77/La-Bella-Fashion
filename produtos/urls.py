from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('produto/<int:produto_id>/', views.detalhes, name='detalhes_produto'),
]
