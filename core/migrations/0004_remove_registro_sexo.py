# Generated by Django 3.2.7 on 2021-10-08 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211008_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='sexo',
        ),
    ]
