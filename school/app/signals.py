from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student

MESSAGE_TEXT = 'Вас успешно создали на сайте School System'


@receiver(post_save, sender=Student)
def send_email_to_student_signals(sender, instance, **kwargs):
    try:
        print(instance.email)
        send_mail(
            subject='School System',
            message=MESSAGE_TEXT,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.email])
    except Exception as e:
        raise Exception(e)
