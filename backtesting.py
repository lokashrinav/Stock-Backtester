# To obtain historical stock data
import yfinance as yf 

#Class backtester will be used for backtesting
class Backtester:
    data = {}

    def __init__(self, start_date, end_date, initial_capital, frequency_of_trades, symbol_list):
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.freqeuncy_of_trades = frequency_of_trades
        self.symbol_list = symbol_list
    
    def import_stock_data():
        for symbol in Backtester.symbol_list:
            Backtester.data[symbol] = yf.download(symbol, start=Backtester.start_date, end=Backtester.end_date)
        return Backtester.data


