# Generated by Django 3.0.8 on 2020-08-19 08:56

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_publish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_time',
            field=django_jalali.db.models.jDateField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
    ]