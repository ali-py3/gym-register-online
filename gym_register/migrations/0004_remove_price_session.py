# Generated by Django 3.2.7 on 2021-09-15 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_register', '0003_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='session',
        ),
    ]
