# Generated by Django 2.2.4 on 2019-09-10 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_seller_stats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='seller_stats',
        ),
    ]
