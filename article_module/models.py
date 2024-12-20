from django.db import models
from account_module.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE,
                               null=True, blank=True,verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200,verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200,unique=True,verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True,verbose_name='فعال / غیرفعال')
    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی  های مقاله'
    def __str__(self):
        return self.title
class Article(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنولن مقاله')
    slug = models.SlugField(max_length=400,db_index=True,allow_unicode=True,verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/articles',verbose_name='تصویر مقاله')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال',default=True)
    selected_categories =models.ManyToManyField(ArticleCategory,verbose_name='دسته بندی ها')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده',null=True,editable=False)
    create_date = models.DateTimeField(auto_now=True,editable=False,verbose_name='تاریخ ثبت')
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقاله ها'
    def __str__(self):
        return self.title

class ArticleComment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='مقاله')
    parent = models.ForeignKey('ArticleComment',on_delete=models.CASCADE,verbose_name='والد',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')
    class Meta:
        verbose_name='نظر مقاله'
        verbose_name_plural='نظرات مقاله '
    def __str__(self):
        return str(self.user)