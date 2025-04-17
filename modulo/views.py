from django.shortcuts import render
from .models import Videojuego, Categoria

def index(request):
    categoria_seleccionada = request.GET.get('categoria', '')
    categorias = Categoria.objects.all()
    
    if categoria_seleccionada:
        videojuegos = Videojuego.objects.filter(categoria_id=categoria_seleccionada)
    else:
        videojuegos = Videojuego.objects.all()
    
    return render(request, 'modulo/index.html', {
        'videojuegos': videojuegos,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada
    })