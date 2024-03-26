import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
            else:
                print("Error: Insufficient quantity of {} shares in the portfolio.".format(symbol))
        else:
            print("Error: {} is not in the portfolio.".format(symbol))

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                total_value += price * quantity
        return total_value

    def get_stock_price(self, symbol):
        api_key = 'BTONO6WLZLCFWTX9'  # Get your API key from Alpha Vantage
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'

        response = requests.get(url)
        data = response.json()
        
        if 'Global Quote' in data:
            return float(data['Global Quote']['05. price'])
        else:
            print(f"Error: Unable to fetch data for {symbol}")
            return None

# Example usage
if __name__ == "__main__":
    portfolio = StockPortfolio()

    # Add stocks to the portfolio
    portfolio.add_stock('AAPL', 10)
    portfolio.add_stock('MSFT', 5)

    # Remove stocks from the portfolio
  #  portfolio.remove_stock('AAPL', 5)

    # Get total portfolio value
    portfolio_value = portfolio.get_portfolio_value()
    print("Total Portfolio Value: $", portfolio_value)
