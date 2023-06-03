# To obtain historical stock data
import yfinance as yf 

#Class backtester will be used for backtesting
class Backtester:
    def __init__(self, start_date, end_date, initial_capital, frequency_of_trades):
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.freqeuncy_of_trades = frequency_of_trades


        

'''Next Steps:
Define Backtester Parameters Just Like in QuantConnect.

Parameter Examples:

1. Start/End Dates
2. Initial Capital
3. Frequency of Trades


'''