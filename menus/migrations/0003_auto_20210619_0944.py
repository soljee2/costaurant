# Generated by Django 2.2 on 2021-06-19 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20210619_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='descripion',
            new_name='description',
        ),
    ]