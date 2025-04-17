from django.contrib import admin
from .models import Categoria, Videojuego

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion')
    list_filter = ('categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'autor')
    ordering = ('titulo',)
    date_hierarchy = 'fecha_publicacion'
