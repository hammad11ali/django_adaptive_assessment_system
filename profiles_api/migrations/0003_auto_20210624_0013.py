# Generated by Django 3.1.1 on 2021-06-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20201020_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
