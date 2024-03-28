from Account import Account

class Investment(Account):
    stockList = {
        "SHOP": [994.70, "CAD"],
        "IBM": [129.87, "USD"],
        "OTEX": [58.44, "CAD"],
        "JD": [60.70, "USD"],
        "MSFT": [196.84, "USD"]
    }

    def __init__(self, owner, currency="CAD", balance=0):
        super().__init__(owner, currency, balance)
        self.cash = balance  
        self.stockHoldings = {}
        for key in self.stockList:
            self.stockHoldings[key] = 0 

    def deposit(self, amount):
        if amount > 0:
            self.cash += amount
            self.balance += amount
        else:
            print("ERROR: Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.cash:
            self.cash -= amount
            self.balance -= amount
        else:
            print("ERROR: Insufficient cash for withdrawal or negative amount")

    def updateStockPrice(self, tickerSymbol, value):
        if tickerSymbol in self.stockList and value >= 0:
            self.stockList[tickerSymbol][0] = value
            total_stock_value = 0 
            for stock in self.stockHoldings:
                stock_price = self.stockList[stock][0]  
                stock_amount = self.stockHoldings[stock] 
                total_stock_value += stock_price * stock_amount 
            self.balance = self.cash + total_stock_value  
        else:
            print("ERROR: Stock price could not be updated!")

    def buy(self, tickerSymbol, amt):
        if tickerSymbol in self.stockList and amt > 0:
            stock_price = self.stockList[tickerSymbol][0]
            total_cost = stock_price * amt
            if self.cash >= total_cost:
                self.stockHoldings[tickerSymbol] += amt
                self.cash -= total_cost
                self.balance -= total_cost
            else:
                print("ERROR: Insufficient cash for stock purchase")
        else:
            print("ERROR: Stock purchase could not be completed!")

    def sell(self, tickerSymbol, amt):
        if tickerSymbol in self.stockList and amt > 0 and self.stockHoldings[tickerSymbol] >= amt:
            stock_price = self.stockList[tickerSymbol][0]
            total_revenue = stock_price * amt
            self.stockHoldings[tickerSymbol] -= amt
            self.cash += total_revenue
            self.balance += total_revenue
        else:
            print("ERROR: Stock sale could not be completed!")
            
    def __str__(self):
        base_str = super().__str__()
        stock_str = "\nStock Holdings:"
        for stock, amt in self.stockHoldings.items():
            stock_str += f"\n{stock} - {amt} @ {self.conversion_rates[self.stockList[stock][1]][1]}{self.stockList[stock][0]} {self.stockList[stock][1]}"
        return base_str + stock_str
