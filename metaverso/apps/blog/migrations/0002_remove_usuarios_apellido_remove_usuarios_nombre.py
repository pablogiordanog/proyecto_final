# Generated by Django 4.2.3 on 2023-07-17 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='nombre',
        ),
    ]