# Generated by Django 5.1.2 on 2024-12-04 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی لینک های فوتر',
                'verbose_name_plural': 'دسته بندی های لینک های فوتر',
            },
        ),
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'verbose_name': 'تنظیمات سایت', 'verbose_name_plural': 'تنظیمات سایت'},
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='address',
            field=models.CharField(max_length=200, verbose_name='ادرس'),
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('fooer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_module.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک  فوتر',
                'verbose_name_plural': ' لینک های فوتر',
            },
        ),
    ]
