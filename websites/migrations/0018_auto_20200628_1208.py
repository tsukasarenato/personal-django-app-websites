# Generated by Django 3.0.7 on 2020-06-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0017_auto_20200628_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colors',
            old_name='cards',
            new_name='cards_hover',
        ),
    ]
