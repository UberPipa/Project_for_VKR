from django.shortcuts import render, redirect
from .models import Docs, TypeDocs
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='authentication')
def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='authentication')
def doc_base(request):
    return render(request, 'main/doc_base.html')


@login_required(login_url='authentication')
def table_1(request):
    docs = Docs.objects.all()
    return render(request, 'main/table_1.html', {'docs': docs})


@login_required(login_url='authentication')
def table_2(request):
    type_docs = TypeDocs.objects.all()
    return render(request, 'main/table_2.html', {'type_docs': type_docs})


def authentication(request):
    if request.user.is_authenticated:
        return redirect('index')
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
    return render(request, 'admin')
