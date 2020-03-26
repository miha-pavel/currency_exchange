from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from celery import shared_task


@shared_task()
def send_mail_task(**kwargs):
    send_mail(
        subject=kwargs['subject'],
        message=kwargs['message'],
        from_email=kwargs['from_email'],
        recipient_list=[settings.EMAIL_HOST_USER],
    )


@shared_task()
def send_activation_code_async(email_to, code):
    path = reverse('activate', args=(code, ))
    send_mail(
        'Your activation code',
        f'http://localhost:8000{path}',
        'fenderoksp@gmail.com',
        [email_to],
        fail_silently=False,
    )
