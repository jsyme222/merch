# Generated by Django 2.2.4 on 2019-08-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_sellerinventory_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerinventory',
            name='last_login',
        ),
        migrations.AddField(
            model_name='sellerinventory',
            name='inventory_title',
            field=models.CharField(default='Default', max_length=250, null=True),
        ),
    ]