from django.shortcuts import render
from .models import Docs, TypeDocs
from django.contrib.auth import login, logout

def index(request):
    docs = Docs.objects.all()
    return render(request, 'main/index.html', {'docs' : docs})


def about(request):
    return render(request, 'main/about.html')


def authentication(request):
    # if request.method == 'POST':
    #     form = UserLoginForm(data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request, user)
    #         return redirect('main/index.html')
    # else:
    #     form = UserLoginForm()
    # return render(request, 'main/authentication.html', {'form': form})
    return render(request, 'main/authentication.html')

def admin(request):
    return render(request, '/admin.html')