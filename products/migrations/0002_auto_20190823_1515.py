# Generated by Django 2.2.4 on 2019-08-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='get_online_img',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='SKU',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
