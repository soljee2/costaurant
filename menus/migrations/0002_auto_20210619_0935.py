# Generated by Django 2.2 on 2021-06-19 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='descripthon',
            new_name='descripion',
        ),
    ]
