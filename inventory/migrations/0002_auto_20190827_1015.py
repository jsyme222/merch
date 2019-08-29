# Generated by Django 2.2.4 on 2019-08-27 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinventory',
            options={'verbose_name_plural': 'Inventories'},
        ),
        migrations.AddField(
            model_name='userinventory',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]