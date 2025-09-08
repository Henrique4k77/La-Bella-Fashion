from django.contrib import admin # Adicione essa linha
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('usuario/', include('usuario.urls')),
]