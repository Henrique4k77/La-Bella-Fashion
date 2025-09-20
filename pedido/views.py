
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .models import Pedido, ItemPedido
import json

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    pedido, _ = Pedido.objects.get_or_create(
        cliente=request.user,
        status='aberto'
    )

    item_pedido, item_criado = ItemPedido.objects.get_or_create(
        pedido=pedido,
        produto=produto,
        defaults={'preco_unitario': produto.preco, 'quantidade': 1}
    )

    if not item_criado:
        item_pedido.quantidade += 1
        item_pedido.save()

    message = f'\"{produto.nome}\" foi adicionado ao seu carrinho.'

    headers = {
        'HX-Trigger': json.dumps({
            'eventoToast': {'message': message}
        })
    }
    return HttpResponse(status=204, headers=headers)

@login_required
def ver_carrinho(request):
    carrinho = Pedido.objects.filter(cliente=request.user, status='aberto').first()
    return render(request, 'pedido/carrinho.html', {'carrinho': carrinho})

@login_required
@require_POST
def atualizar_quantidade(request, item_id):
    item_pedido = get_object_or_404(ItemPedido, id=item_id, pedido__cliente=request.user)
    message = ''
    try:
        nova_quantidade = int(request.POST.get('quantidade'))
        if nova_quantidade > 0:
            item_pedido.quantidade = nova_quantidade
            item_pedido.save()
            # Mensagem de atualização removida para não gerar toast
        elif nova_quantidade <= 0:
            nome_produto = item_pedido.produto.nome
            item_pedido.delete()
            # Mensagem de remoção mantida para gerar o toast
            message = f'\"{nome_produto}\" foi removido do seu carrinho.'

    except (ValueError, TypeError):
        pass # Nenhum erro é enviado ao usuário, a página apenas atualiza
    
    carrinho = Pedido.objects.filter(cliente=request.user, status='aberto').first()
    response = render(request, 'pedido/partials/carrinho_detail.html', {'carrinho': carrinho})
    
    # O gatilho do toast só será adicionado se a mensagem (de remoção) existir
    if message:
        response['HX-Trigger'] = json.dumps({'eventoToast': {'message': message}})
    
    return response

@login_required
@require_POST
def remover_do_carrinho(request, item_id):
    item_pedido = get_object_or_404(ItemPedido, id=item_id, pedido__cliente=request.user)
    nome_produto = item_pedido.produto.nome
    item_pedido.delete()
    
    message = f'\"{nome_produto}\" foi removido do seu carrinho.'
    
    carrinho = Pedido.objects.filter(cliente=request.user, status='aberto').first()
    response = render(request, 'pedido/partials/carrinho_detail.html', {'carrinho': carrinho})
    response['HX-Trigger'] = json.dumps({'eventoToast': {'message': message}})
    
    return response

@login_required
def finalizar_pedido(request):
    carrinho = Pedido.objects.filter(cliente=request.user, status='aberto').first()
    
    if carrinho and carrinho.itens.all().exists():
        carrinho.status = 'finalizado'
        carrinho.save()
        messages.success(request, f"Pedido #{carrinho.id} finalizado com sucesso!")
        return redirect('pedido:detalhe_pedido', pedido_id=carrinho.id)
    
    messages.error(request, "Seu carrinho está vazio. Adicione itens antes de finalizar.")
    return redirect('catalogo')


@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.filter(cliente=request.user).exclude(status='aberto').order_by('-data_pedido')
    return render(request, 'pedido/lista_pedidos.html', {'pedidos': pedidos})

@login_required
def detalhe_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, cliente=request.user)
    return render(request, 'pedido/detalhe_pedido.html', {'pedido': pedido})
