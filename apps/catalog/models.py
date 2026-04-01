from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    titulo = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    descripcion = models.TextField("Descripción")
    imagen = models.ImageField("Imagen", upload_to="catalog/categories/")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)
    destacado = models.BooleanField("Destacado", default=False)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["orden"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class GalleryImage(models.Model):
    categoria = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Categoría",
    )
    imagen = models.ImageField("Imagen", upload_to="catalog/gallery/")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Imagen de galería"
        verbose_name_plural = "Imágenes de galería"
        ordering = ["orden"]

    def __str__(self):
        return f"{self.categoria.titulo} - Imagen {self.orden}"
