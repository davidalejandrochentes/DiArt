from django.db import models


class Tienda(models.Model):
    foto = models.ImageField(upload_to='tienda/')
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tienda'

    def save(self, *args, **kwargs):
        if not self.pk and Tienda.objects.exists():
            raise ValueError('Solo puede existir un registro de Tienda')
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'Tienda'


class CategoriaTienda(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, related_name='categorias')
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    imagen = models.ImageField(upload_to='tienda/categorias/')
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(CategoriaTienda, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    slug = models.SlugField()
    descripcion = models.TextField()
    precio_normal = models.DecimalField(max_digits=10, decimal_places=2)
    precio_rebajado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='tienda/productos/')
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['orden', 'nombre']
        unique_together = ['categoria', 'slug']

    def __str__(self):
        return self.nombre

    @property
    def precio_actual(self):
        return self.precio_rebajado if self.precio_rebajado else self.precio_normal
