from django.shortcuts import render
from pedido.models import Pedido

def home(request):
    if request.user.is_authenticated:
        carrinho_aberto = Pedido.objects.filter(cliente=request.user, status='carrinho').first()
        if carrinho_aberto:
            carrinho_count = carrinho_aberto.itens.count()
        else:
            carrinho_count = 0
    else:
        carrinho_count = 0

    return render(request, 'home.html', {'carrinho_count': carrinho_count})

def login(request):
    return render(request, 'login.html')

def cadastrar_usuario(request):
    return render(request, 'cadastrar.html')

def meus_dados(request):
    usuario = {
        'nome': 'Henrique',
        'email': 'henrique@email.com',
        'ra': '101100101',
        'turma': 'pro (manhã)',
        'telefone': '11986941564',
    }
    return render(request, 'meus_dados.html', {'usuario': usuario})

def editar_dados(request):
    usuario = {
        'nome': 'Henrique',
        'email': 'henrique@email.com',
        'ra': '101100101',
        'turma': 'pro (manhã)',
        'telefone': '11986941564',
    }
    return render(request, 'editar_dados.html', {'usuario': usuario})

def excluir_perfil(request):
    usuario = {
        'nome': 'Henrique',
    }
    return render(request, 'excluir_perfil.html', {'usuario': usuario})