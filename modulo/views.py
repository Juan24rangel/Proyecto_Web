from django.shortcuts import render, get_object_or_404, redirect
from .models import Videojuego, Categoria, Comentario

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

def detalle_videojuego(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)
    comentarios = videojuego.comentarios.order_by('-fecha')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        texto = request.POST.get('texto')
        if nombre and texto:
            Comentario.objects.create(videojuego=videojuego, nombre=nombre, texto=texto)
            return redirect('detalle_videojuego', videojuego_id=videojuego.id)
    return render(request, 'modulo/detalle_videojuego.html', {
        'videojuego': videojuego,
        'comentarios': comentarios
    })