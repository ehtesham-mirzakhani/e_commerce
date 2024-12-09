from django.db import models
from django.utils.text import slugify


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان",db_index=True)
    url_title = models.CharField(max_length=100,verbose_name="عنوان در url",db_index=True)
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفعال بودن')
    is_delete = models.BooleanField(verbose_name='حذف شده/نشده',default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'
class ProductBrand(models.Model):
    title = models.CharField(max_length=300,verbose_name='نام برند',db_index=True)
    url_title = models.CharField(max_length=300,verbose_name='نام در url',db_index=True)
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال ')
    class Meta:
        verbose_name='برند'
        verbose_name_plural='برند ها'
    def __str__(self):
        return self.title
class Product(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان')
    category = models.ManyToManyField(ProductCategory,verbose_name='دسته بندی ها',
                                 related_name='products', blank=True)
    image = models.ImageField(upload_to='images/products',null=True,blank=True,verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductBrand,on_delete=models.CASCADE,verbose_name='برند',null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=500,null=True,verbose_name='توضیحات کوتاه',db_index=True)
    description = models.TextField(verbose_name='توضیحات اصلی',db_index=True)
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفعال ')
    is_delete = models.BooleanField(verbose_name='حذف شده/نشده',default=False)
    slug = models.SlugField(max_length=200, unique=True,null=False,blank=True,db_index=True,verbose_name='عنوان در url')
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class ProductTag(models.Model):
    caption = models.CharField( max_length=50,db_index=True, verbose_name='تگ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_tags')
    class Meta:
        verbose_name='تگ محصول'
        verbose_name_plural='تگ محصولات'
    def __str__(self):
        return self.caption