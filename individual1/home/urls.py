from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bienvenida, name='blog-home'),
    path('contacto/', views.contacto, name='contacto-home'),
    path('logIn/', views.logIn, name='logIn-home'),
    path('logOut/', views.logOut, name='logOut-home'),
    path('registro/', views.registro, name='registro-home')
]