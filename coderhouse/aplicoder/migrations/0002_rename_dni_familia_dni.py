# Generated by Django 4.0.3 on 2022-04-07 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familia',
            old_name='DNI',
            new_name='dni',
        ),
    ]
