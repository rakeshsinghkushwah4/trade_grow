from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from angle_stocks.models import Stock, Delivery
import requests
import pdb
from stocks_api import settings
from angle_stocks.stock_data import get_history_data, get_current_data, get_delivery_data
from angle_stocks.indicators import Indicator
import csv
from datetime import date


# Create your views here.

def stocks(request):
    # url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
    # result = requests.get(url).json()
    # # pdb.set_trace()
    # insert = []
    # for i in result:
    #     if i["symbol"].split("-")[-1]=="EQ" and i["instrumenttype"]=="" and i["exch_seg"]=="NSE":
    #         insert.append(Stock(token=i["token"], symbol=i["symbol"], name=i["name"]))
    # # Stock.objects.bulk_create(insert)
    # file = open('/home/developer/Downloads/EQUITY_L.csv')
    # stock_data = []
    # for i in csv.reader(file):
    #     stock_data.append(Stock(symbol= i[0], name= i[1]))
    # Stock.objects.bulk_create(stock_data)
    return HttpResponse('This is my home page')

# def Home(request):
#     stocks = Stock.objects.all
#     context = {"stocks": stocks}
#     return render(request, 'home/index.html', context)

# def GetStockData(request, token):
#     co_data = get_history_data("^NSEI", "1d", "115d")
#     ba_data = get_history_data("ADANIGREEN.NS", "1d", "115d")
#     data = Indicator().RS(ba_data['close'], co_data['close'], 12)
#     context = {"stock_data": data}
#     return render(request, 'stock_detail.html', context)


def RS(request):
  stocks = Stock.objects.all()
  co_data = get_history_data("^NSEI", "1d", "115d")
  for i in stocks:
    try:
        ba_data = get_history_data("{i}.NS".format(i = i.symbol), "1d", "115d")
        data21 = Indicator().RS(ba_data['close'], co_data['close'], 21)
        data55 = Indicator().RS(ba_data['close'], co_data['close'], 55)
        print(i,data21[0], data55[0])
        i.rs_55 = data55[0]
        i.rs_21 = data21[0]
        i.save()
    except:
        print(">>>>>>>>>>", "{i}.NS".format(i = i.symbol))
  return redirect('update_data')

def DeliveryData(request):
  date = request.POST['delivery_date']
  final_date = "".join(date.split("-")[::-1])
  data = get_delivery_data(final_date)
  for i in data:
    d = i.split(",")
    if d[3] == "EQ":
      try:
        stock = Stock.objects.get(symbol=d[2])
        Delivery.objects.create(stock=stock, traded_quantity=d[4], delivery_quantity=d[5], delivery_percentage=float(d[6]), delivery_date=date)
      except: 
        print(">>>>>>>>>>>>>>>>>>>>>>>")
  return redirect('update_data')

def DeliveryDelete(request):
  date = request.POST['delivery_date']
  Delivery.objects.filter(delivery_date=date).delete()
  return redirect('update_data')


def ChartData(request, symbol, interval = "1d", interval_range = "1y"):
  data = get_history_data("{i}.NS".format(i = symbol), interval, interval_range)
  return JsonResponse(data)



  # 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