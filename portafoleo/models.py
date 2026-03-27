from django.db import models


class Portafolio(models.Model):
    foto = models.ImageField(upload_to='portafolio/')
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolio'

    def save(self, *args, **kwargs):
        if not self.pk and Portafolio.objects.exists():
            raise ValueError('Solo puede existir un registro de Portafolio')
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'Portafolio'


class CategoriaPortafolio(models.Model):
    portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE, related_name='categorias')
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    imagen = models.ImageField(upload_to='portafolio/categorias/')
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class ImagenCategoria(models.Model):
    categoria = models.ForeignKey(CategoriaPortafolio, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='portafolio/galeria/')
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Imagen de galería'
        verbose_name_plural = 'Imágenes de galería'
        ordering = ['orden']

    def __str__(self):
        return f'Imagen {self.id} - {self.categoria.nombre}'
