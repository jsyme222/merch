# Generated by Django 2.2.4 on 2019-08-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant', models.CharField(max_length=150, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=100, null=True)),
                ('account_user', models.CharField(blank=True, max_length=150, null=True)),
                ('account_pass', models.CharField(blank=True, max_length=150, null=True)),
                ('url', models.CharField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('wholesale', models.DecimalField(decimal_places=2, max_digits=6)),
                ('resale', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=6, null=True)),
                ('profit', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=6, null=True)),
                ('QTY', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Merchant')),
            ],
        ),
    ]
