# Importing the yfinance library for historical stock data
import yfinance as yf

# Class Backtester will be used for backtesting
class Backtester:

    def __init__(self, start_date, end_date, initial_capital, frequency_of_trades, symbol_list):
        # Initializing the Backtester class with the specified parameters
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.frequency_of_trades = frequency_of_trades
        self.symbol_list = symbol_list
    
    def import_stock_data(self):
        # A dictionary to store the historical stock data
        data = {}
        # Method to import historical stock data for each symbol in symbol_list
        for symbol in self.symbol_list:
            # Downloading historical stock data using yfinance and storing it in the data dictionary based on symbol as key
            data[symbol] = yf.download(symbol, start=self.start_date, end=self.end_date)
            # Checks if any specific value is missing for the symbol
            if data[symbol].isna().any().any():
                # Outputs Warning Message based on missing data for symbol
                print(f"Warning: Missing data found for symbol {symbol}")
                # Removing rows with missing values. Plan to remove specific values later
                data[symbol] = data[symbol].dropna() 

        return data

bt = Backtester(start_date='2022-01-01', end_date='2022-12-31', initial_capital=100000, frequency_of_trades=10, symbol_list=['AAPL', 'MSFT'])

stock_data = bt.import_stock_data()

print(stock_data)
    
