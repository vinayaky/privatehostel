# Generated by Django 4.2.1 on 2023-05-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default=False, max_length=250, null=True, upload_to='images/')),
                ('imagepname', models.CharField(max_length=100)),
            ],
        ),
    ]
