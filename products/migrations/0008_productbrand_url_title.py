# Generated by Django 5.1.2 on 2024-12-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='url_title',
            field=models.CharField(db_index=True, default='url_title', max_length=300, verbose_name='نام در url'),
            preserve_default=False,
        ),
    ]
