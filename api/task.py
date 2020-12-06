from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task(duration):
    send_mail('Celery worked','Celery is cool','ar9786@gmail.com',['arvind.rawat@kiwitech.com'],fail_silently=False)
    return None