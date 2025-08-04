from .models import Categoria

def categorias(request):
    return {
        'categorias': Categoria.objects.all().order_by('nombre'),
        'categorias_cultura': Categoria.objects.filter(tipos__nombre='Cultura').order_by('nombre'),
        'categorias_eventos': Categoria.objects.filter(tipos__nombre='Eventos').order_by('nombre'),
        'categorias_galeria': Categoria.objects.filter(tipos__nombre='Galeria').order_by('nombre'),
    }