# Generated by Django 4.2.1 on 2023-05-18 13:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='/home/cseiei/Code/python/Digi-Backend/theboi.gif', max_length=255, verbose_name='image'),
        ),
    ]