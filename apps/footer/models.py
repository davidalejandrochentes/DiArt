from django.db import models


class Footer(models.Model):
    logo = models.ImageField("Logo", upload_to="footer/", blank=True, null=True)
    descripcion = models.TextField("Descripción")
    direccion = models.CharField("Dirección", max_length=300)
    telefono = models.CharField("Teléfono", max_length=50)
    email = models.EmailField("Email")
    horario = models.CharField("Horario de atención", max_length=200)
    copyright = models.CharField("Copyright", max_length=200)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

    def __str__(self):
        return "Footer"

    def save(self, *args, **kwargs):
        if Footer.objects.exists() and not self.pk:
            existing = Footer.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)


class SocialLink(models.Model):
    PLATFORM_ICONS = {
        "facebook": "facebook",
        "instagram": "instagram",
        "twitter": "twitter",
        "linkedin": "linkedin",
        "youtube": "youtube",
        "whatsapp": "whatsapp",
        "tiktok": "tiktok",
    }

    plataforma = models.CharField("Plataforma", max_length=50)
    url = models.URLField("URL")
    icono = models.CharField(
        "Icono",
        max_length=50,
        blank=True,
        help_text="Nombre del icono: facebook, instagram, twitter, linkedin, youtube, whatsapp, tiktok",
    )
    orden = models.PositiveIntegerField("Orden", default=0)
    activo = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ["orden"]

    def __str__(self):
        return self.plataforma
