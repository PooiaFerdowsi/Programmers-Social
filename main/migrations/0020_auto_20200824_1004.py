# Generated by Django 3.0.8 on 2020-08-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_person_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='آواتار'),
        ),
    ]