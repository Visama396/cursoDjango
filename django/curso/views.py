from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactoForm


def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    enviado = False
    if request.method == "POST":
        f = ContactoForm(request.POST)
        if f.is_valid():
            f.save()
            enviado = True
    else:
        f = ContactoForm()

    context = {"form": f,
               "enviado": enviado}
    return render(request, 'contact.html', context)


def elements(request):
    return render(request, 'elements.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def services(request):
    return render(request, 'services.html')


def hola(request, nombre):
    return render(request, 'hola.html', {'nombre': nombre})

