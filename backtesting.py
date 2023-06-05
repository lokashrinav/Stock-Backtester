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
        self.data = {}
    
    def import_stock_data(self):
        # A dictionary to store the historical stock data
        # Method to import historical stock data for each symbol in symbol_list
        for symbol in self.symbol_list:
            # Downloading historical stock data using yfinance and storing it in the data dictionary based on symbol as key
            self.data[symbol] = yf.download(symbol, start=self.start_date, end=self.end_date)
            # Checks if any specific value is missing for the symbol
            if self.data[symbol].isna().any().any():
                # Outputs Warning Message based on missing data for symbol
                print(f"Warning: Missing data found for symbol {symbol}")
                # Removing rows with missing values. Plan to remove specific values later
                self.data[symbol] = self.data[symbol].dropna() 
        return self.data

    def strategy(self):
        # Implementing a basic pair trading strategy under the assumption of 2 symbols in symbol list
        close_prices_1 = self.data[self.symbol_list[0]]['Close']
        close_prices_2 = self.data[self.symbol_list[1]]['Close']
            
        # Calculating the standard deviation of the 'Close' prices
        std1 = close_prices_1.std(ddof=0)
        std2 = close_prices_2.std(ddof=0)

        z_score = (close_prices_1 - close_prices_2) / (std1 + std2)

        if z_score > 1.0:
            return 'SELL'
        elif z_score < -1.0:
            return 'BUY'
        elif abs(z_score) < 0.5:
            return 'CLOSE'

        return 'HOLD'

    # Executes trades
    def trades():
        pass


    # Runs everything
    def run():
        pass

        

bt = Backtester(start_date='2022-01-01', end_date='2022-12-31', initial_capital=100000, frequency_of_trades=10, symbol_list=['AAPL', 'MSFT'])

stock_data = bt.import_stock_data()

print(stock_data)
    
