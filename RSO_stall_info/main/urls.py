from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('authentication', views.authentication, name='authentication'),
    path('logout', views.logoutUser, name='logout'),
    path('admin', admin.site.urls, name='admin')
]
