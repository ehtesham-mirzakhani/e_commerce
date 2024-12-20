# Generated by Django 5.1.2 on 2024-11-19 08:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=100, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال بودن')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده/نشده')),
            ],
            options={
                'verbose_name': 'دسته بندی محصول',
                'verbose_name_plural': 'دسته بندی محصولات',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز')),
                ('short_description', models.CharField(db_index=True, max_length=500, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال بودن')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده/نشده')),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('category', models.ManyToManyField(blank=True, related_name='product_categories', to='products.productcategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=50, verbose_name='تگ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='products.product')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ محصولات',
            },
        ),
    ]
