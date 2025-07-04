# Generated by Django 5.1.7 on 2025-04-09 15:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_film_list_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film_list',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='film_list',
            name='id',
        ),
        migrations.RemoveField(
            model_name='film_list',
            name='image',
        ),
        migrations.RemoveField(
            model_name='film_list',
            name='seats',
        ),
        migrations.AlterField(
            model_name='film_list',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('seats', models.IntegerField(default=50)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film_list')),
            ],
        ),
    ]
