# Generated by Django 4.0.6 on 2022-07-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angle_stocks', '0007_alter_stock_rs_21_alter_stock_rs_55'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='close_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Close Price'),
        ),
        migrations.AddField(
            model_name='stock',
            name='high_price',
            field=models.FloatField(blank=True, null=True, verbose_name='High Price'),
        ),
        migrations.AddField(
            model_name='stock',
            name='low_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Low Price'),
        ),
        migrations.AddField(
            model_name='stock',
            name='open_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Open Price'),
        ),
    ]
