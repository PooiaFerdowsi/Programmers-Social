# Generated by Django 3.0.8 on 2020-08-19 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200818_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
    ]