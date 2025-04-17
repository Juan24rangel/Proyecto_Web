from django.db import models

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

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"
