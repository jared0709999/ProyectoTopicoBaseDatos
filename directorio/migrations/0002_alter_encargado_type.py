# Generated by Django 3.2.7 on 2021-11-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encargado',
            name='type',
            field=models.CharField(choices=[('Administracion', 'Administracion'), ('Pedagogia', 'Pedagogia'), ('Fomento a la Salud', 'Fomento a la Salud'), ('Alimentación', 'Alimentación')], max_length=50, verbose_name='Area'),
        ),
    ]
