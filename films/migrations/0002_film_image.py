# Generated by Django 5.1.7 on 2025-04-09 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
