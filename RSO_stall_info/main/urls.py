from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('doc_base', views.doc_base, name='doc_base'),
    path('authentication', views.authentication, name='authentication'),
    path('logout', views.logoutUser, name='logout'),
    path('admin', admin.site.urls, name='admin'),
    #path('table_1', views.table_1, name='table_1'),
]
