# Generated by Django 4.0.6 on 2022-07-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angle_stocks', '0009_stock_cr_date_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateField(unique=True, verbose_name='Delivery Date'),
        ),
    ]