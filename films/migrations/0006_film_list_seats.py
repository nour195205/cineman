# Generated by Django 5.1.7 on 2025-04-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_film_list_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='film_list',
            name='seats',
            field=models.IntegerField(default=50, max_length=2),
        ),
    ]
