from django.contrib import admin
from django.urls import  include, path
from . import views

urlpatterns = [

    path('', views.index, name = 'index'),
    path('inicio/', views.inicio, name = 'inicio'),
    path('forgotPassword/', views.forgotPassword),
    path('register/', views.register),
    path('reloads/', views.reloads),
    path('movements/', views.movements),
    path('routes/', views.routes),
    path('profile/', views.profile),
    path('pqrs/', views.pqrs),
    path('contactus/', views.contactus),
]
