# Generated by Django 5.1.2 on 2024-12-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0008_alter_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت'),
        ),
    ]