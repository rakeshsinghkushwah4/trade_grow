from django.db import models
from angle_stocks.models import Stock


# Create your models here.

class BookMark(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.stock


class PaperTrade(models.Model):
    stock = models.CharField(max_length=225, null=True, blank=True, verbose_name="Stock Symbol")
    strategy = models.CharField(max_length=225, null=True, blank=True, verbose_name="Strategy")
    entry = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Entry price")
    exit_price = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Exit price")
    target = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Target price")
    stop_loss = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Stop Loss")
    target_hit = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Target Hit")
    stop_loss_hit = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Stop loss Hit")
    resion = models.TextField(null=True, blank=True, verbose_name="Resion To Buy")
    image = models.ImageField(upload_to='images/')
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock

class TradeJournal(models.Model):
    stock = models.CharField(max_length=225, null=True, blank=True, verbose_name="Stock Symbol")
    strategy = models.CharField(max_length=225, null=True, blank=True, verbose_name="Strategy")
    quantity = models.IntegerField(null=True, blank=True, verbose_name="Quantity")
    entry = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Entry price")
    exit_price = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Exit price")
    target = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Target price")
    stop_loss = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Stop Loss")
    target_hit = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Target Hit")
    stop_loss_hit = models.FloatField(max_length=225, null=True, blank=True, verbose_name="Stop loss Hit")
    resion = models.TextField(null=True, blank=True, verbose_name="Resion To Buy")
    image = models.ImageField(upload_to='images/')
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock

