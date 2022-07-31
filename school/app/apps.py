from django.apps import AppConfig
from django.db.models.signals import post_save


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from .models import Student
        from .signals import send_email_to_student_signals
        post_save.connect(send_email_to_student_signals, sender=Student)
