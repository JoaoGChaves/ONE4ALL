from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Cadastro

def pagina_index(request):
    return render(request, 'index.html')

def pagina_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha1 = request.POST.get('password')
        usuario = authenticate(request, email = email, password = senha1)
        print(usuario,)
        if usuario is not None:
            login(request, usuario)
            return redirect('pagamento')
        else:
            messages.error (request, 'Usuario ou senha incorretos.')
    return render(request, 'login.html')

def pagina_cadastro(request):
    if request.method == 'POST':
        nomeOrg = request.POST.get('nomeOrg')
        nomeResp = request.POST.get('nomeResp')
        cnpj = request.POST.get('cnpj')
        telefone = request.POST.get('tel')
        email = request.POST.get('email')
        senha1 = request.POST.get('senha')
        senha2 = request.POST.get('confirmar')

        if senha1 == senha2:
            meu_usuario = Cadastro(
                nomeOrg=nomeOrg,
                nomeResp=nomeResp,
                cnpj=cnpj,
                telefone=telefone,
                email=email,
                senha=senha1
            )
            meu_usuario.save()
            print(meu_usuario)
            return redirect('login')
    return render(request, 'cadastro.html')

def pagina_pagamento(request):
    return render(request, 'pagamento.html')

