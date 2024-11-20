from django.db import models

# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان')
    name = models.CharField(max_length=100,verbose_name="نام")
    email = models.EmailField(max_length=300,verbose_name="ایمیل")
    message = models.TextField(verbose_name='متن تماس با ما')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    response = models.TextField(verbose_name='متن پاسخ تماس با ما',blank=True,null=True)
    is_read_by_admin = models.BooleanField(default=False,verbose_name='خوانده شده توسط ادمین')
    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='لیست تماس با ما'
    def __str__(self):
        return self.title