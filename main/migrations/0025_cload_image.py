# Generated by Django 3.0.8 on 2020-08-26 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_post_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, upload_to='cload/images/', verbose_name='فایل')),
            ],
        ),
        migrations.CreateModel(
            name='cload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space', models.CharField(default=100, max_length=3, verbose_name='فضا')),
                ('used_space', models.CharField(default=0, max_length=3, verbose_name='فضای استفاده شده')),
                ('available', models.CharField(default=100, max_length=3, verbose_name='فضای باقیمانده')),
                ('files', models.ManyToManyField(to='main.image')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person', verbose_name='صاحب')),
            ],
        ),
    ]