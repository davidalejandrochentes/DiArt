from django.db import models


class TeamMember(models.Model):
    nombre = models.CharField("Nombre", max_length=200)
    cargo = models.CharField("Cargo", max_length=200)
    imagen = models.ImageField("Imagen", upload_to="team/")
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Miembro del equipo"
        verbose_name_plural = "Miembros del equipo"
        ordering = ["orden"]

    def __str__(self):
        return self.nombre
