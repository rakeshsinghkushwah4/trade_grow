from django.shortcuts import render
from angle_stocks.models import Stock, Delivery

# Create your views here.

def Home(request):
    # stocks = Stock.objects.filter(rs_55__gte=0)
    stocks = Stock.objects.all()
    context = {"stocks": stocks}
    return render(request, 'user_interface/index.html', context)

def UpdateData(request):
    return render(request, 'user_interface/update_data.html')

def DeliveryList(request, stock):
    stock = Stock.objects.get(symbol=stock)
    deliveries = Delivery.objects.filter(stock= stock).order_by('-delivery_date')
    context = {'deliveries': deliveries}
    return render(request, 'user_interface/delivery_list.html', context)

def PaperTrade(request):
    return render(request, 'user_interface/forms')