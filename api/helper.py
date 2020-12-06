from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail('Celery worked','Celery is cool','ar9786@gmail.com',['arvind.rawat@kiwitech.com'],fail_silently=False)
    return None