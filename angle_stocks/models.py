from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=225, null=True, blank=True, verbose_name="Stock Symbol")
    name = models.CharField(max_length=225, null=True, blank=True, verbose_name="Stock name")
    open_price = models.FloatField(null=True, blank=True, verbose_name="Open Price") 
    high_price = models.FloatField(null=True, blank=True, verbose_name="High Price")
    low_price = models.FloatField(null=True, blank=True, verbose_name="Low Price")
    close_price = models.FloatField(null=True, blank=True, verbose_name="Close Price")
    cr_date = models.DateTimeField(auto_now_add=True)
    rs_55 = models.FloatField(null=True, blank=True, verbose_name="Relative Strength 55")
    rs_21 = models.FloatField(null=True, blank=True, verbose_name="Relative Strength 21")

    
    def __str__(self):
        return self.symbol


class Delivery(models.Model):
    delivery_date = models.DateField(verbose_name="Delivery Date")
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    delivery_quantity = models.IntegerField(null=True, blank=True, verbose_name="Delivery Quantity")
    delivery_percentage = models.FloatField(null=True, blank=True, verbose_name="Delivery Percentage")
    traded_quantity = models.IntegerField(null=True, blank=True, verbose_name="Traded Quantity")
    # vwap use next day price is trade above vwap or make graph of vwap and delivery quantity
    vwap = models.FloatField(null=True, blank=True, verbose_name="VWAP")
    
    class Meta:
        unique_together = ('stock', 'delivery_date')

    def __int__(self):
        return self.stock