from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils import timezone
class User(AbstractUser):
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    mobile_number = models.IntegerField(max_length=11,default=0, verbose_name='شماره تلفن')
    address = models.CharField(max_length=300, blank=True, verbose_name='آدرس')
    natioral_code = models.IntegerField(max_length=10,default=0, verbose_name='کد ملی')
    date_birth = models.CharField(max_length=10, verbose_name="تاریخ تولد")

    class Meta:
        verbose_name_plural = "کاربر ها"
        verbose_name = "کاربر ها"


class Tuition(models.Model):
    session = models.CharField(max_length=250, verbose_name='جلسه')
    tiotion = models.IntegerField(verbose_name='شهریه')


    def __str__(self):
        return self.session
    class Meta:
        verbose_name_plural = "شهریه و جلسات"

