from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Contact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    message_file = models.FileField(
        blank=True, null=True,
        upload_to='messages/')

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f'{self.email}'
