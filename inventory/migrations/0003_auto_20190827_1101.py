# Generated by Django 2.2.4 on 2019-08-27 17:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0002_auto_20190827_1015'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInventory',
            new_name='SellerInventory',
        ),
    ]
