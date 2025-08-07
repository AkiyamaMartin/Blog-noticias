from django.shortcuts import render
from articulos.models import Articulo
from agenda.models import Evento
from datetime import date

def home(request):
    ultimos_articulos = Articulo.objects.filter().order_by('-creado')[:6] #solo 6
    
    proximos_eventos = Evento.objects.filter(fecha__gte=date.today()).order_by('fecha', 'hora')[:3] #Last 3
     
    contexto = {
        'ultimos_articulos': ultimos_articulos,
        'proximos_eventos': proximos_eventos,
    }
    
    return render(request, 'home.html', contexto)