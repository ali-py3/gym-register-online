# Generated by Django 3.2.7 on 2021-09-15 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_register', '0004_remove_price_session'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
    ]
