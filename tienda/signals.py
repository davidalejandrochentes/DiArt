import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Tienda, CategoriaTienda, Producto


def eliminar_imagen(ruta_imagen):
    if ruta_imagen:
        ruta_completa = os.path.join(settings.MEDIA_ROOT, str(ruta_imagen))
        if os.path.isfile(ruta_completa):
            os.remove(ruta_completa)


@receiver(post_delete, sender=Tienda)
def eliminar_imagen_tienda(sender, instance, **kwargs):
    if instance.foto:
        eliminar_imagen(instance.foto)


@receiver(pre_save, sender=Tienda)
def eliminar_imagen_anterior_tienda(sender, instance, **kwargs):
    if instance.pk:
        try:
            anterior = Tienda.objects.get(pk=instance.pk)
            if anterior.foto and anterior.foto != instance.foto:
                eliminar_imagen(anterior.foto)
        except Tienda.DoesNotExist:
            pass


@receiver(post_delete, sender=CategoriaTienda)
def eliminar_imagen_categoria(sender, instance, **kwargs):
    if instance.imagen:
        eliminar_imagen(instance.imagen)


@receiver(pre_save, sender=CategoriaTienda)
def eliminar_imagen_anterior_categoria(sender, instance, **kwargs):
    if instance.pk:
        try:
            anterior = CategoriaTienda.objects.get(pk=instance.pk)
            if anterior.imagen and anterior.imagen != instance.imagen:
                eliminar_imagen(anterior.imagen)
        except CategoriaTienda.DoesNotExist:
            pass


@receiver(post_delete, sender=Producto)
def eliminar_imagen_producto(sender, instance, **kwargs):
    if instance.imagen:
        eliminar_imagen(instance.imagen)


@receiver(pre_save, sender=Producto)
def eliminar_imagen_anterior_producto(sender, instance, **kwargs):
    if instance.pk:
        try:
            anterior = Producto.objects.get(pk=instance.pk)
            if anterior.imagen and anterior.imagen != instance.imagen:
                eliminar_imagen(anterior.imagen)
        except Producto.DoesNotExist:
            pass
