from django.shortcuts import render, get_object_or_404
from .models import Produto

def catalogo(request):
    produtos = Produto.objects.all()
    return render(request, 'catalogo.html', {'produtos': produtos})

def detalhes(request, produto_id):

    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'detalhes.html', {'produto': produto})
