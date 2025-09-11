from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

def cadastrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # cria usuário se não existir
        if User.objects.filter(username=username).exists():
            return render(request, 'cadastrar.html', {'erro': 'Nome de usuário já existe'})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # loga automaticamente depois de cadastrar
        auth_login(request, user)
        return redirect('meus_dados')  # redireciona para página de dados
    return render(request, 'cadastrar.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('meus_dados')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')


@login_required
def meus_dados(request):
    return render(request, 'meus_dados.html', {'usuario': request.user})
