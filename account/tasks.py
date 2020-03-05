from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task


@shared_task()
def send_mail_task(**kwargs):
    send_mail(
        subject=kwargs['subject'],
        message=kwargs['message'],
        from_email=kwargs['from_email'],
        recipient_list=[settings.EMAIL_HOST_USER],
    )
