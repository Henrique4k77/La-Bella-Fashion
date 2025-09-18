from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, PerfilUpdateForm, UserRegistrationForm, PerfilRegistrationForm
from .models import Perfil

def cadastrar(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        perfil_form = PerfilRegistrationForm(request.POST)

        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            perfil = perfil_form.save(commit=False)
            perfil.usuario = user
            perfil.save()

            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            return redirect('usuario_login')
        else:
            # Adiciona erros dos formulários às mensagens para depuração
            if user_form.errors:
                for field, error in user_form.errors.items():
                    messages.error(request, f"{field}: {error}")
            if perfil_form.errors:
                for field, error in perfil_form.errors.items():
                    messages.error(request, f"{field}: {error}")

    else:
        user_form = UserRegistrationForm()
        perfil_form = PerfilRegistrationForm()

    return render(
        request,
        'cadastrar.html',
        {
            'user_form': user_form,
            'perfil_form': perfil_form
        }
    )

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
    perfil, criado = Perfil.objects.get_or_create(usuario=request.user)
    return render(
        request,
        'meus_dados.html',
        {
            'usuario': request.user,
            'perfil': perfil
        }
    )


@login_required
def editar_dados(request):
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
        return redirect('usuario_login')
    
    return render(request, 'excluir_perfil.html', {'usuario': request.user})


def sair(request):
    auth_logout(request)
    return redirect('usuario_login')
