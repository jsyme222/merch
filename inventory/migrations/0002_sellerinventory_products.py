# Generated by Django 2.2.4 on 2019-09-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerinventory',
            name='products',
            field=models.ManyToManyField(to='products.Merchandise'),
        ),
    ]