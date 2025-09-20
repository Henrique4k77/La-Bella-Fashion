from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    
    # Novas URLs para manipular o carrinho
    path('carrinho/remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/atualizar/<int:item_id>/', views.atualizar_quantidade, name='atualizar_quantidade'),
    
    path('finalizar/', views.finalizar_pedido, name='finalizar_pedido'),
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('<int:pedido_id>/', views.detalhe_pedido, name='detalhe_pedido'),
]
