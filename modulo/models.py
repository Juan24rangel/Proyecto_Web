from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Videojuego(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    ISBN = models.CharField(max_length=13, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='videojuegos/', null=True, blank=True)  # Nuevo campo
    sinopsis = models.TextField(null=True, blank=True)  # Nuevo campo

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"

class Comentario(models.Model):
    videojuego = models.ForeignKey('Videojuego', on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    rating = models.IntegerField(default=0)  # Si usas estrellas
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario en {self.videojuego.titulo} - {self.texto[:30]}"

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    videojuego = models.ForeignKey('Videojuego', on_delete=models.CASCADE, related_name='favoritos')
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.videojuego.titulo}"
