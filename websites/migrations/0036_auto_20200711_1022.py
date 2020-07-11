# Generated by Django 3.0.7 on 2020-07-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0035_auto_20200711_1008'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='products',
            constraint=models.UniqueConstraint(fields=('websites', 'slug'), name='unique_product'),
        ),
    ]