# Generated by Django 3.2.7 on 2021-09-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_register', '0008_alter_user_natioral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.IntegerField(default=0, verbose_name='شماره تلفن'),
        ),
    ]