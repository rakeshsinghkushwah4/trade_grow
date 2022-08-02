from stocks_api import settings
import pdb


class Indicator:
    
    def RS(self, base_data, comper_data, time_period):
        base_data = base_data[::-1]
        comper_data = comper_data[::-1]
        result = []
        if len(base_data) == len(comper_data):
            # when you want 12 days RS data so we have request 24days data just double  
            for i in range(0, time_period):
                rs = base_data[i] / base_data[i+(time_period-1)] / (comper_data[i] / comper_data[i+(time_period-1)]) - 1
                result.append(round(rs, 2))
        return result




# https://query2.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=I1JO.jRwfFR&lang=en-US&region=US&symbols=ADANIGREEN.NS&fields=messageBoardId%2ClongName%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2CtoCurrency%2CfromCurrency%2CtoExchange%2CfromExchange&corsDomain=finance.yahoo.com
# https://query2.finance.yahoo.com/v7/finance/quote?formatted=true&symbols=ADANIGREEN.NS&longName,shortName,marketCap,underlyingSymbol,underlyingExchangeSymbol?headSymbolAsString,regularMarketPrice,regularMarketChange,regularMarketChangePercent,regularMarketVolume,regularMarketOpen,fiftyTwoWeekLow,fiftyTwoWeekHigh,toCurrency,fromCurrency,toExchange,fromExchange

        



    
    