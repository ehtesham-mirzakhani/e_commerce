# Generated by Django 5.1.2 on 2024-11-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر محصول'),
        ),
    ]