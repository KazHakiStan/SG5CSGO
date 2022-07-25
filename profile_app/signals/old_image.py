import os
from django.db.models.signals import pre_save
from django.dispatch import receiver
from profile_app.models import Profile


@receiver(pre_save, sender=Profile)
def old_image(sender, instance, **kwargs):
    if not instance.pk:
        return False
    if sender.objects.get(pk=instance.pk).photo:

        image_old = sender.objects.get(pk=instance.pk).photo

        image_new = instance.photo

        if image_old != image_new:
            if os.path.isfile(image_old.path):
                os.remove(image_old.path)
        else:
            return False