# Generated by Django 5.1.2 on 2024-12-17 16:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0002_alter_order_options_alter_orderdetail_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='نهایی شده/نشده'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='count',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='تعداد'),
        ),
    ]