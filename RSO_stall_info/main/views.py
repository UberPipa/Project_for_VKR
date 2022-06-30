from django.shortcuts import render, redirect
from .models import Docs, TypeDocs
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def index(request):
    docs = Docs.objects.all()
    return render(request, 'main/index.html', {'docs': docs})


def about(request):
    return render(request, 'main/about.html')


def authentication(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Неверно указан логин или пароль')
    context = {}
    return render(request, 'main/authentication.html', context)


def logoutUser(request):
    logout(request)
    return redirect('authentication')


def admin(request):
    return render(request, '/admin.html')
