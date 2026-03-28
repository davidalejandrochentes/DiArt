import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Header


@receiver(pre_save, sender=Header)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Header.objects.get(pk=instance.pk)
    except Header.DoesNotExist:
        return

    if old_instance.imagen and old_instance.imagen != instance.imagen:
        old_path = os.path.join(settings.MEDIA_ROOT, old_instance.imagen.name)
        if os.path.isfile(old_path):
            os.remove(old_path)


@receiver(post_delete, sender=Header)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.imagen:
        image_path = os.path.join(settings.MEDIA_ROOT, instance.imagen.name)
        if os.path.isfile(image_path):
            os.remove(image_path)
