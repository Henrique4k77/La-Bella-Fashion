# djangoapp/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings # Importe as configurações do projeto
from django.conf.urls.static import static # Importe a função static

urlpatterns = [
    path('admin/', admin.site.urls),

    # página inicial
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # todas as URLs do app usuario
    path('usuario/', include('usuario.urls')),
]

# Configuração para servir arquivos de mídia apenas em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)