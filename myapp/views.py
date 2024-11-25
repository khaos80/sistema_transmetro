from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')

def inicio(request):
    return render(request, 'inicio.html')

def forgotPassword(request):
    return render(request, 'forgotPassword.html')

def register(request):
    return render(request, 'register.html')

def reloads(request):
    return render(request, 'reloads.html')

def movements(request):
    return render(request, 'movements.html')

def routes(request):
    return render(request, 'routes.html')

def profile(request):
    return render(request, 'profile.html')

def pqrs(request):
    return render(request, 'pqrs.html')

def contactus(request):
    return render(request, 'contactus.html')
    