from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def services(request):
    return render(request, 'services.html')


def hola(request, nombre):
    return render(request, 'hola.html', {'nombre': nombre})

