# Generated by Django 2.2.4 on 2019-08-28 21:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190827_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
