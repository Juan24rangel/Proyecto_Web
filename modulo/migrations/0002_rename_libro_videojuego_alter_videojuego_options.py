# Generated by Django 5.1.7 on 2025-04-17 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Libro',
            new_name='Videojuego',
        ),
        migrations.AlterModelOptions(
            name='videojuego',
            options={'verbose_name': 'Videojuego', 'verbose_name_plural': 'Videojuegos'},
        ),
    ]
