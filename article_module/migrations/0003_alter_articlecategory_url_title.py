# Generated by Django 5.1.2 on 2024-12-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0002_alter_articlecategory_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='url_title',
            field=models.CharField(max_length=200, unique=True, verbose_name='عنوان در url'),
        ),
    ]