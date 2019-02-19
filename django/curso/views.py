from django.http import HttpResponse
from django.shortcuts import render


def hola(request, nombre):
    return render(request, 'hola.html', {'nombre': nombre})

