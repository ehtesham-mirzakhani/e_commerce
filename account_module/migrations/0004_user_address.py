# Generated by Django 5.1.2 on 2024-12-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس'),
        ),
    ]