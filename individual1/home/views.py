from django.shortcuts import render
from django.http import HttpResponse
import datetime
import locale

# Create your views here.
publicaciones=[
    {
        'autor':"Rodrigo",
        'titulo': "Publicacion 1",
        'contenido': "loremp ipsum",
        'fecha': "13 de julio del 2023"
    },
    {
        'autor':"Nicolas",
        'titulo': "Publicacion 2",
        'contenido': "loremp ipsum 2",
        'fecha': "13 de julio del 2023"
    },
    {
        'autor':"Adolfo",
        'titulo': "Publicacion 3",
        'contenido': "loremp ipsum 3",
        'fecha': "13 de julio del 2023"
    }
]

def bienvenida(request):
    contexto = {
        'publicaciones': publicaciones
    }
    return render(request,'home/index.html', contexto)

def contacto(request):
    return render (request, 'home/contacto.html',{'titulo': 'aweklab'})

def logIn(request):
    locale.setlocale(locale.LC_TIME, 'es_ES')
    time= datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S').capitalize
    return render (request,'home/logIn.html',{'time':time})

def logOut(request):
    return render (request, 'home/logOut.html')

def registro(request):
    return render (request, 'home/registro.html')