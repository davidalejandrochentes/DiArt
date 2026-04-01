from django.db import models


class About(models.Model):
    texto_general = models.TextField("Texto general")
    proyectos_completados = models.PositiveIntegerField(
        "Proyectos completados", default=0
    )
    anios_experiencia = models.PositiveIntegerField("Años de experiencia", default=0)
    clientes_felices = models.PositiveIntegerField("Clientes felices", default=0)
    mision = models.TextField("Misión")
    vision = models.TextField("Visión")
    imagen_1 = models.ImageField("Imagen principal", upload_to="about/")
    imagen_2 = models.ImageField("Imagen secundaria", upload_to="about/")

    class Meta:
        verbose_name = "Sobre Nosotros"
        verbose_name_plural = "Sobre Nosotros"

    def __str__(self):
        return "Sobre Nosotros"

    def save(self, *args, **kwargs):
        if About.objects.exists() and not self.pk:
            existing = About.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)
