#!/usr/bin/env python

class Stock(object):
    """docstring for Stock"""
    def __init__(self, name = '', symbol = '', price = 0.0, payout = 0.0):
        super(Stock, self).__init__()
        self.name = name
        self.symbol = symbol
        self.price = price
        self.payout = payout

    def __str__(self):
        return self.name + "\'s symbol is " + self.symbol + " with a price of $" + str(self.price) + " and a payout of $" + str(self.payout)

    def __lt__(self, second):
        return self.price < second.price

    def __eq__(self, second):
        return self.price == second.price

    def __gt__(self, second):
        return self.price > second.price

    def __ne__(self, second):
        return self.price != second.price

if __name__ == '__main__':
    # more here
    google = Stock("Alphabet", "GOOG", 400.0, 0.0)
    microsoft = Stock("Microsoft", "MSFT", 52.00, 5)
    apple = Stock("Apple", "AAPL", 105, 5)
    yahoo = Stock("Yahoo", "YHOO", 33, 0)
    stocks = [google, microsoft, apple, yahoo]
    stocks = sorted(stocks)
    for stock in stocks:
        print stock
