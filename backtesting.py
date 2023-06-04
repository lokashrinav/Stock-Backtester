# Importing the yfinance library for retrieving historical stock data
import yfinance as yf

# Class Backtester will be used for backtesting
class Backtester:
    # A dictionary to store the downloaded stock data
    data = {}

    def __init__(self, start_date, end_date, initial_capital, frequency_of_trades, symbol_list):
        # Initializing the Backtester class with the specified parameters
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.frequency_of_trades = frequency_of_trades
        self.symbol_list = symbol_list
    
    def import_stock_data():
        # Method to import historical stock data for each symbol in the symbol list
        for symbol in Backtester.symbol_list:
            # Downloading historical stock data using yfinance and storing it in the data dictionary
            Backtester.data[symbol] = yf.download(symbol, start=Backtester.start_date, end=Backtester.end_date)
        return Backtester.data