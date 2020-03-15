from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User


@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, **kwargs):
    instance_pk = instance.pk
    if instance_pk:
        try:
            old_avatar = User.objects.get(id=instance_pk).avatar
        except User.DoesNotExist:
            return
        else:
            new_avatar = instance.avatar
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)
