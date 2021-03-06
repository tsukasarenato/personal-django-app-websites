# Generated by Django 3.0.7 on 2020-06-21 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0005_auto_20200620_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 16, 29, 33, 700693)),
        ),
        migrations.AlterField(
            model_name='websites',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 16, 29, 33, 595756)),
        ),
        migrations.AlterField(
            model_name='websites',
            name='url',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]
