# Generated by Django 5.0.1 on 2024-01-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='tamano',
            field=models.CharField(choices=[('grande', 'Grande'), ('mediano', 'Mediano'), ('chico', 'Chico')], default='Mediano', max_length=10),
            preserve_default=False,
        ),
    ]
