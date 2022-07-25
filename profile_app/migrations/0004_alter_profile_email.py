# Generated by Django 4.0.4 on 2022-07-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, unique=True, verbose_name='email'),
        ),
    ]