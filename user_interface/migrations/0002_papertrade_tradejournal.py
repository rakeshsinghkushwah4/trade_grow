# Generated by Django 4.0.6 on 2022-07-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(blank=True, max_length=225, null=True, verbose_name='Stock Symbol')),
                ('strategy', models.CharField(blank=True, max_length=225, null=True, verbose_name='Strategy')),
                ('entry', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Entry price')),
                ('exit_price', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Exit price')),
                ('target', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Target price')),
                ('stop_loss', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Stop Loss')),
                ('target_hit', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Target Hit')),
                ('stop_loss_hit', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Stop loss Hit')),
                ('resion', models.TextField(blank=True, null=True, verbose_name='Resion To Buy')),
                ('image', models.ImageField(upload_to='images/')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TradeJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(blank=True, max_length=225, null=True, verbose_name='Stock Symbol')),
                ('strategy', models.CharField(blank=True, max_length=225, null=True, verbose_name='Strategy')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('entry', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Entry price')),
                ('exit_price', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Exit price')),
                ('target', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Target price')),
                ('stop_loss', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Stop Loss')),
                ('target_hit', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Target Hit')),
                ('stop_loss_hit', models.FloatField(blank=True, max_length=225, null=True, verbose_name='Stop loss Hit')),
                ('resion', models.TextField(blank=True, null=True, verbose_name='Resion To Buy')),
                ('image', models.ImageField(upload_to='images/')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
