# Generated by Django 4.2.1 on 2023-06-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_images_image_images_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='uid',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
