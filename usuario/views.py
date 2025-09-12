from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, PerfilUpdateForm # Importação corrigida
from .models import Perfil # Adicione esta importação para o Perfil

def cadastrar(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not username or not email or not password:
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'cadastrar.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'cadastrar.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return render(request, 'cadastrar.html')

        # Crie o usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Crie um objeto Perfil para o novo usuário
        Perfil.objects.create(usuario=user)

        messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
        return redirect('usuario_login')

    return render(request, 'cadastrar.html')


def login(request):
    if request.method == 'POST':
        login_input = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        username_to_auth = login_input

        if '@' in login_input:
            try:
                user_by_email = User.objects.get(email=login_input)
                username_to_auth = user_by_email.username
            except User.DoesNotExist:
                messages.error(request, 'Usuário ou senha inválidos.')
                return render(request, 'login.html')

        user = authenticate(request, username=username_to_auth, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('meus_dados')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html')

    return render(request, 'login.html')


@login_required
def meus_dados(request):
    # A view agora tentará obter ou criar o Perfil do usuário para evitar o erro 'DoesNotExist'
    perfil, criado = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'meus_dados.html', {'usuario': request.user})


@login_required
def editar_dados(request):
    # Passamos a instância do usuário e do seu perfil para os formulários
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)
        
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, 'Seus dados foram atualizados com sucesso!')
            return redirect('meus_dados')
    else:
        user_form = UserUpdateForm(instance=request.user)
        # O Perfil será criado se não existir, evitando um erro
        perfil, criado = Perfil.objects.get_or_create(usuario=request.user)
        perfil_form = PerfilUpdateForm(instance=perfil)
    
    context = {
        'user_form': user_form,
        'perfil_form': perfil_form
    }
    
    return render(request, 'editar_dados.html', context)


@login_required
def excluir_perfil(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Seu perfil foi excluído com sucesso.')
        return redirect('logout') # Redireciona para o login após a exclusão
    
    return render(request, 'excluir_perfil.html', {'usuario': request.user})


def sair(request):
    auth_logout(request)
    return redirect('usuario_login')