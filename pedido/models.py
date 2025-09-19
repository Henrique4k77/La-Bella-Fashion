
from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto

STATUS_OPCOES = [
    ('aberto', 'Em aberto'),
    ('finalizado', 'Finalizado'),
    ('pago', 'Pago'),
    ('enviado', 'Enviado'),
]

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_OPCOES, default='aberto')

    @property
    def total(self):
        return sum(item.total_item for item in self.itens.all())

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.username} - {self.status}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_item(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome} no Pedido #{self.pedido.id}'
