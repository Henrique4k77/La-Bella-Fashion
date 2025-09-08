# usuario/views.py
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')