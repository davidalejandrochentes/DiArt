import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Portafolio, CategoriaPortafolio, ImagenCategoria


def eliminar_imagen(ruta_imagen):
    if ruta_imagen:
        ruta_completa = os.path.join(settings.MEDIA_ROOT, str(ruta_imagen))
        if os.path.isfile(ruta_completa):
            os.remove(ruta_completa)


@receiver(post_delete, sender=Portafolio)
def eliminar_imagen_portafolio(sender, instance, **kwargs):
    if instance.foto:
        eliminar_imagen(instance.foto)


@receiver(pre_save, sender=Portafolio)
def eliminar_imagen_anterior_portafolio(sender, instance, **kwargs):
    if instance.pk:
        try:
            anterior = Portafolio.objects.get(pk=instance.pk)
            if anterior.foto and anterior.foto != instance.foto:
                eliminar_imagen(anterior.foto)
        except Portafolio.DoesNotExist:
            pass


@receiver(post_delete, sender=CategoriaPortafolio)
def eliminar_imagen_categoria(sender, instance, **kwargs):
    if instance.imagen:
        eliminar_imagen(instance.imagen)


@receiver(pre_save, sender=CategoriaPortafolio)
def eliminar_imagen_anterior_categoria(sender, instance, **kwargs):
    if instance.pk:
        try:
            anterior = CategoriaPortafolio.objects.get(pk=instance.pk)
            if anterior.imagen and anterior.imagen != instance.imagen:
                eliminar_imagen(anterior.imagen)
        except CategoriaPortafolio.DoesNotExist:
            pass


@receiver(post_delete, sender=ImagenCategoria)
def eliminar_imagen_galeria(sender, instance, **kwargs):
    if instance.imagen:
        eliminar_imagen(instance.imagen)


@receiver(pre_save, sender=ImagenCategoria)
def eliminar_imagen_anterior_galeria(sender, instance, **kwargs):
    if instance.pk:
        try:
            anterior = ImagenCategoria.objects.get(pk=instance.pk)
            if anterior.imagen and anterior.imagen != instance.imagen:
                eliminar_imagen(anterior.imagen)
        except ImagenCategoria.DoesNotExist:
            pass
