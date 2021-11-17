"""Within it, define a new class called Portfolio which:

has a method called buy, which adds a new stock to the portfolio, taking 3 arguments

name, a str, the symbol of the stock which is being bought

shares, an int, the quantity which is being bought

price, a float, the price paid per share

and has a second method called cost which returns a float, the total cost paid for all stocks in the portfolio

Consider that to implement the cost method, you'll need to be storing the purchases made each time the buy method is called somewhere. You may do so by any means convenient to you.
"""

"""
def __init__(self,name,shares,price,somename=[]):
    self.name = str(name)
    self.shares = int(shares)
    self.price = float(price)
    self.somename = somename

def __buy__(self,names1,shares1,price1,somename):
    self.names1 = names1
    self.shares1 = shares1
    self.price1 = price1
    self.somename = somename.append((self.names1, self.shares1, self.price1))

def __cost__(self,amount):
    self.amount = float(amount)

(self.names1, self.prices1, self.price1)
 self.price_value = price_value.append(price)
 _price_addition_(self, values_list=[], final_sum=0):
	self.final_sum = final_sum
	self.values_list = values_list
	for i in len(values_list):
		final_sum = final_sum+values_list(i)
	return final_sum

"""

class Portfolio:

    def __init__(self):
        self._stocks = []

    def buy(self,name,shares,price):
        self._stocks.append((name,shares,price))

    def cost(self):
        return sum(
            shares * price for name, shares, price in self._stocks
        )

