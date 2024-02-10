# Generated by Django 4.2.8 on 2023-12-13 06:55

from django.db import migrations, models
import pereval.services


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pereval.services.get_path_upload_images, verbose_name='Изображение'),
        ),
    ]