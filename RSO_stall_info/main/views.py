from django.shortcuts import render
from .models import Docs, TypeDocs

def index(request):
    docs = Docs.objects.all()
    return render(request, 'main/index.html', {'docs' : docs})


def about(request):
    return render(request, 'main/about.html')


def about(request):
    return render(request, 'main/authentication.html')
