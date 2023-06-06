# Generated by Django 4.2.1 on 2023-05-17 18:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
