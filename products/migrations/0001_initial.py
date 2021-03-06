# Generated by Django 2.2.4 on 2019-08-26 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(blank=True, default='', max_length=250, null=True, unique=True)),
                ('wholesale', models.DecimalField(decimal_places=2, max_digits=6)),
                ('resale', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Suggested retail')),
                ('profit', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=6, null=True)),
                ('img', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Merchandise',
            },
        ),
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vender', models.CharField(max_length=150, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=100, null=True)),
                ('account_user', models.CharField(blank=True, max_length=150, null=True)),
                ('account_pass', models.CharField(blank=True, max_length=150, null=True)),
                ('url', models.CharField(blank=True, max_length=550, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VenderMerchandise',
            fields=[
                ('merchandise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Merchandise')),
                ('online_info', models.BooleanField(default=False, help_text='*If selected the information for the product will be \t\tgathered from the merchants website if available', verbose_name='Get info from website?*')),
            ],
            options={
                'verbose_name_plural': 'Vender Merchandise',
            },
            bases=('products.merchandise',),
        ),
    ]
