# Generated by Django 4.0.6 on 2022-07-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angle_stocks', '0011_alter_delivery_delivery_date_alter_delivery_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_percentage',
            field=models.FloatField(blank=True, null=True, verbose_name='Delivery Percentage'),
        ),
    ]
