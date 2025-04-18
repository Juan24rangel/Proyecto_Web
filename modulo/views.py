from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Videojuego, Categoria, Comentario, Favorito, Perfil
from .forms import FotoPerfilForm

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
    comentarios = videojuego.comentarios.order_by('-fecha')  # Ordenar por fecha descendente
    es_favorito = False

    if request.user.is_authenticated:
        es_favorito = Favorito.objects.filter(usuario=request.user, videojuego=videojuego).exists()

    if request.method == 'POST':
        texto = request.POST.get('texto')
        rating = request.POST.get('rating')  # Si usas estrellas
        if texto:
            Comentario.objects.create(videojuego=videojuego, texto=texto, rating=rating)
            return redirect('detalle_videojuego', videojuego_id=videojuego.id)

    return render(request, 'modulo/detalle_videojuego.html', {
        'videojuego': videojuego,
        'comentarios': comentarios,
        'es_favorito': es_favorito,  # Pasar al template
    })

@login_required
def perfil(request):
    perfil = Perfil.objects.get_or_create(usuario=request.user)[0]  # Obtén o crea el perfil
    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = FotoPerfilForm(instance=perfil)
    return render(request, 'modulo/perfil.html', {'user': request.user, 'form': form, 'perfil': perfil})

@login_required
def agregar_favorito(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)
    if not Favorito.objects.filter(usuario=request.user, videojuego=videojuego).exists():
        Favorito.objects.create(usuario=request.user, videojuego=videojuego)
    return redirect('detalle_videojuego', videojuego_id=videojuego.id)

@login_required
def eliminar_favorito(request, videojuego_id):
    videojuego = get_object_or_404(Videojuego, id=videojuego_id)
    Favorito.objects.filter(usuario=request.user, videojuego=videojuego).delete()
    return redirect('detalle_videojuego', videojuego_id=videojuego.id)

def index(request):
    query = request.GET.get('q')  # Obtén el término de búsqueda desde el formulario
    if query:
        videojuegos = Videojuego.objects.filter(titulo__icontains=query)  # Búsqueda insensible a mayúsculas
        if not videojuegos.exists():
            mensaje = "Este videojuego aún no está registrado."
        else:
            mensaje = None
    else:
        videojuegos = Videojuego.objects.all()
        mensaje = None

    return render(request, 'modulo/index.html', {
        'videojuegos': videojuegos,
        'mensaje': mensaje,
    })