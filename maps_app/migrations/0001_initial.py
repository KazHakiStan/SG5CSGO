# Generated by Django 4.0.4 on 2022-07-03 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('pos_name', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
    ]
