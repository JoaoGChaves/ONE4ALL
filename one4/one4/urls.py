"""
URL configuration for one4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_one import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.pagina_index, name='inicial'),
  path('login/', views.pagina_login, name='login'),
  path('cadastro/', views.pagina_cadastro, name='cadastro'),
  path('pagamento/', views.pagina_pagamento, name='pagamento'),
  path('doacaoMensal/', views.pagina_mensal, name='mensal'),
  path('doacaoUnica/', views.pagina_unica, name= 'unica'),
  path('queroAjuda/', views.pagina_ajuda, name= 'ajuda'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)