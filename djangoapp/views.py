from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

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