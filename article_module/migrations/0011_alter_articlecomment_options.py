# Generated by Django 5.1.2 on 2024-12-07 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0010_articlecomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecomment',
            options={'verbose_name': 'نظر مقاله', 'verbose_name_plural': 'نظرات مقاله '},
        ),
    ]
