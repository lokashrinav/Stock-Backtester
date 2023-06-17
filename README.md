# Stock-Backtester

Backtester
 - The Backtester is a Python class that allows you to backtest a basic pair trading strategy using historical stock data. It utilizes the yfinance library to import the historical stock data for the specified symbols.

Features
 - Import historical stock data for a given date range and symbol list.
 - Implement a basic pair trading strategy based on the historical data.
 - Execute trades based on the strategy and keep track of the trades made.
 - Calculate the z-score to determine the trading actions (BUY, SELL, CLOSE, or HOLD).
 - Import the yfinance library: import yfinance as yf.
 - Create an instance of the Backtester class, specifying the start and end dates, initial capital, trading frequency, and symbol list.
 - Run the backtest using the run method.
 - Access the executed trades through the trades attribute.

# Create an instance of the Backtester class
backtester = Backtester(start_date='2022-01-01', end_date='2022-12-31', initial_capital=100000, frequency_of_trades=10, symbol_list=['AAPL', 'MSFT'])

# Run the backtest
trades = backtester.run()

# Access the executed trades
for trade in trades:
    print(trade)
Feel free to customize the parameters according to your specific requirements.

Requirements
Python 3.6 or higher
yfinance library
Make sure to install the yfinance library before running the backtester:

Copy code
pip install yfinance
Disclaimer
The Backtester is a tool for educational and informational purposes only. It does not guarantee any specific investment results or profits. Use it at your own risk.

License
This project is licensed under the MIT License.
