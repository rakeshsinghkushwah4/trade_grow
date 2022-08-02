# Generated by Django 4.0.6 on 2022-07-22 16:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('angle_stocks', '0008_stock_close_price_stock_high_price_stock_low_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='cr_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_quantity', models.IntegerField(blank=True, null=True, verbose_name='Delivery Quantity')),
                ('delivery_date', models.DateField(verbose_name='Delivery Date')),
                ('delivery_percentage', models.IntegerField(blank=True, null=True, verbose_name='Delivery Percentage')),
                ('traded_quantity', models.IntegerField(blank=True, null=True, verbose_name='Traded Quantity')),
                ('vwap', models.FloatField(blank=True, null=True, verbose_name='VWAP')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angle_stocks.stock')),
            ],
        ),
    ]