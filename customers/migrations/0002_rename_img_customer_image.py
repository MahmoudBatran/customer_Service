# Generated by Django 4.1 on 2022-08-18 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='img',
            new_name='image',
        ),
    ]
