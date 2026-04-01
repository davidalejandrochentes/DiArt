import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import About


@receiver(pre_save, sender=About)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = About.objects.get(pk=instance.pk)
    except About.DoesNotExist:
        return

    for field in ["imagen_1", "imagen_2"]:
        old_image = getattr(old_instance, field)
        new_image = getattr(instance, field)
        if old_image and old_image != new_image:
            old_path = os.path.join(settings.MEDIA_ROOT, old_image.name)
            if os.path.isfile(old_path):
                os.remove(old_path)
