# Generated by Django 4.0.4 on 2022-07-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
    ]
