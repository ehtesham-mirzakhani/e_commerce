from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date, datetime, timedelta
from django.utils import timezone

class User(AbstractUser):
    first_name = models.CharField(max_length=120,verbose_name='نام')
    last_name = models.CharField(max_length=120,verbose_name='نام خانوادگی')
    avatar = models.ImageField(upload_to='images/profile',null=True, blank=True,verbose_name='تصویر اواتار')
    email = models.EmailField(unique=True,verbose_name="ایمیل")
    address = models.TextField(null=True,blank=True,verbose_name='ادرس')
    username = models.CharField(verbose_name='نام کاربری',max_length=20,unique=True)
    phone = models.CharField(max_length=50,verbose_name='تلفن',null=True, blank=True,unique=True)
    about_user = models.TextField(null=True, blank=True,verbose_name='درباره شخص')
    active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل', default='default_value')
    created_at = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    def save(self, *args, **kwargs):
        self.expire_date = timezone.now() + timedelta(minutes=1)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.username
    def is_expire(self):
        return  timezone.now() > self.expire_date