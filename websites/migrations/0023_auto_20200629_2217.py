# Generated by Django 3.0.7 on 2020-06-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0022_auto_20200629_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=20, null=True),
        ),
    ]