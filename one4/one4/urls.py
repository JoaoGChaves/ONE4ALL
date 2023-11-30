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
  path('', views.pagina_inicio, name='inicio'),
  path('login/', views.pagina_login, name='login'),
  path('cadastro/', views.pagina_cadastro, name='cadastro'),
  path('doacaoMensal/', views.pagina_mensal, name='mensal'),
  path('doacaoUnica/', views.pagina_unica, name= 'unica'),
  path('queroAjuda/', views.pagina_queroAjudar, name= 'ajuda'),
  path('sobrenos/', views.pagina_sobrenos, name= 'sobrenos'),
  path('pagamento1/', views.pagina_pagamento1, name= 'pagamento1'),
  path('pagamento2/', views.pagina_pagamento2, name= 'pagamento2'),
  path('pagamento3/', views.pagina_pagamento3, name= 'pagamento3'),
  path('feed/', views.pagina_feed, name= 'feed'),
  path('tabela/', views.pagina_tabela, name= 'tabela'),
  path('confirmacao/', views.pagina_confirmacao, name= 'confirmacao'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)