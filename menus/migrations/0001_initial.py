# Generated by Django 2.2 on 2021-06-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('name_eng', models.CharField(max_length=80)),
                ('descripthon', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('img_path', models.CharField(max_length=255)),
            ],
        ),
    ]
