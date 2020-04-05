from uuid import uuid4
from datetime import datetime
from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

from .tasks import send_activation_code_async, send_activation_sms_code_async


def avatar_path(instance, file_name):
    ext = file_name.split('.')[-1]
    filename = f'{str(uuid4())}.{ext}'
    print('filename: ', '/'.join(['avatar', filename]))
    return '/'.join(['avatar', filename])


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")
    
    avatar = models.ImageField(upload_to=avatar_path, null=True, blank=True, default=None)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

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


class ActivationCode(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activation_codes')
    created = models.DateTimeField(auto_now_add=True)
    code = models.UUIDField(default=uuid4, editable=False, unique=True)
    is_activated = models.BooleanField(default=False)

    @property
    def is_expired(self):
        now = datetime.now()
        diff = now - self.created
        return diff.days > 7

    def send_activation_code(self):
        send_activation_code_async.delay(self.user.email, self.code)


class ActivationCodeSMS(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activation_sms_codes')
    created = models.DateTimeField(auto_now_add=True)
    code = models.PositiveSmallIntegerField(default=randint(1000, 32767))
    is_activated = models.BooleanField(default=False)

    @property
    def is_expired(self):
        now = datetime.now()
        diff = now - self.created
        return diff.days > 7

    def send_activation_sms_code(self):
        send_activation_sms_code_async.delay(self.user.phone, self.code)
