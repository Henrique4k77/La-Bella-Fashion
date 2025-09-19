from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    # Visualiza o carrinho (pedido em aberto)
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),

    # Adiciona um produto ao carrinho
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),

    # Finaliza o pedido (muda o status do carrinho)
    path('finalizar/', views.finalizar_pedido, name='finalizar_pedido'),

    # Lista os pedidos finalizados
    path('', views.lista_pedidos, name='lista_pedidos'),

    # Detalhes de um pedido específico
    path('<int:pedido_id>/', views.detalhe_pedido, name='detalhe_pedido'),
]
