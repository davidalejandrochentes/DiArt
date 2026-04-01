from django.db import models


class Service(models.Model):
    titulo = models.CharField("Título", max_length=200)
    descripcion_corta = models.CharField("Descripción corta", max_length=150)
    descripcion_larga = models.TextField("Descripción larga")
    imagen = models.ImageField("Imagen", upload_to="services/")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["orden"]

    def __str__(self):
        return self.titulo
