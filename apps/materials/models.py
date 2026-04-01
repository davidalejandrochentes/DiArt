from django.db import models
from django.utils.text import slugify


class MaterialCategory(models.Model):
    titulo = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    descripcion = models.TextField("Descripción")
    imagen = models.ImageField("Imagen", upload_to="materials/categories/")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)
    destacado = models.BooleanField("Destacado", default=False)

    class Meta:
        verbose_name = "Categoría de Material"
        verbose_name_plural = "Categorías de Materiales"
        ordering = ["orden"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class Product(models.Model):
    categoria = models.ForeignKey(
        MaterialCategory,
        on_delete=models.CASCADE,
        related_name="productos",
        verbose_name="Categoría",
    )
    nombre = models.CharField("Nombre", max_length=200)
    slug = models.SlugField("Slug", blank=True)
    descripcion = models.TextField("Descripción")
    imagen = models.ImageField("Imagen", upload_to="materials/products/")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["orden"]

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
