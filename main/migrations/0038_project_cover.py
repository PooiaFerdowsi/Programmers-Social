# Generated by Django 3.0.8 on 2020-08-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20200829_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cover',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='کاور'),
        ),
    ]