# Generated by Django 4.0.6 on 2022-07-29 18:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='username',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+996777777777'.", regex='^\\+?1?\\d{9,12}$')]),
        ),
    ]
