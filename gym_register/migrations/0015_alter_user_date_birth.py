# Generated by Django 3.2.7 on 2021-09-20 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gym_register', '0014_alter_user_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.DateField(default=django.utils.timezone.localtime, verbose_name='تاریخ تولد'),
        ),
    ]
