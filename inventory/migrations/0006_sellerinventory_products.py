# Generated by Django 2.2.4 on 2019-08-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190827_1235'),
        ('inventory', '0005_auto_20190827_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerinventory',
            name='products',
            field=models.ManyToManyField(to='products.Merchandise'),
        ),
    ]
