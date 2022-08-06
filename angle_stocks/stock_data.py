from stocks_api import settings
from angle_stocks.external_urls import ExternalUrls
import requests
import pdb


# interval=1wk
# range=1y
# https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI?region=US&lang=en-US&includePrePost=false&interval=1h&useYfid=true&range=1mo&corsDomain=finance.yahoo.com&.tsrc=finance
# data['chart']['result'][0]['indicators']['quote'][0]['open]

def get_current_data(symbol, interval, stock_range):
  data = get_data(symbol, interval, stock_range)
  return data['meta']['regularMarketPrice']

def get_history_data(symbol, interval, stock_range):
  data = get_data(symbol, interval, stock_range)
  timestamp = data['timestamp']
  price_data = data['indicators']['quote'][0]
  volume = price_data['volume']
  price_open = price_data['open']
  low = price_data['low']
  close = price_data['close']
  high = price_data['high']
  return { "open": price_open, "low": low, "close": close, "high": high, "volume": volume, "timestamp": timestamp }
    

    
def get_data(symbol, interval, stock_range):
  url = ExternalUrls.yahoo_url(symbol, interval, stock_range)
  response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
  data = response.json()
  return data['chart']['result'][0]

def get_delivery_data(date):
  url = ExternalUrls.delivery_url(date)
  response = requests.get(url)
  data = response.text.split("\n")[4:-1]
  return data


# Download Delivery Data and save
# d = requests.get("url")
# data = d.text.split("\n")
# data[4] return stock data
