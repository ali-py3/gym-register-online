# Generated by Django 3.2.7 on 2021-09-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_register', '0012_auto_20210920_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.TimeField(verbose_name='تاریخ تولد'),
        ),
    ]
