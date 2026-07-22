from django.conf import settings
from django.core.mail import send_mail

def send_email_to_client(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
        fail_silently=False,
    )