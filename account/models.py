from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models


def avatar_path(instance, file_name):
    ext = file_name.split('.')[-1]
    filename = f'{str(uuid4)}.{ext}'
    return '/'.join(['avatar', filename])


class User(AbstractUser):
    avatar = models.ImageField(upload_to=avatar_path, null=True, blank=True, default=None)

    def __str__(self):
        return self.username


class Contact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f'{self.email}'
