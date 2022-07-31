from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .managers import TeacherManager


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    birthday = models.DateField()
    classroom = models.ForeignKey('Class',
                                  on_delete=models.CASCADE)  # Если удалить объект Класса, у ученика тоже не будет класса
    address = models.CharField(max_length=256)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='student_photos', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(AbstractUser):
    username = None
    phone_number = models.CharField(validators=[
        RegexValidator(regex=r'^\+?1?\d{9,12}$',
                       message="Phone number must be entered in the format: '+996777777777'.")
    ], max_length=13, unique=True)
    subject_name = models.CharField(max_length=250)
    objects = TeacherManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"Phone: {self.phone_number}"


class Class(models.Model):
    title = models.CharField(max_length=150)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey('School', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class School(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
