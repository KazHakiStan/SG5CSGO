# Generated by Django 4.0.4 on 2022-07-03 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='pos_name',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
