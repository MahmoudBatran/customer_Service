# Generated by Django 4.1 on 2022-08-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='edited_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
