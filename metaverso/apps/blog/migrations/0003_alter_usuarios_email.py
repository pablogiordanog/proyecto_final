# Generated by Django 4.2.3 on 2023-07-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_usuarios_apellido_remove_usuarios_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
