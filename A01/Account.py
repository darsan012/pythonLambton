# creating classes for the users
class Account:
    def __init__(self, owner, currency = "CAD", balance = 0):
         # dictonaries for the currency conversions

        self.conversion_rates = {
                'USD': [1.34607, '$'],
                'EUR': [1.51746, '€'],
                'GBP': [1.70233, '£'],
                'CNY': [0.0189917, '¥'],
                'INR': [0.0178035, '₹'],
                'CAD': [1, '$']
            }

        self.owner = owner
        self.balance = balance
        if currency in self.conversion_rates:
            self._currency = currency
        else:
             print("ERROR: Unsupported currency type")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("ERROR: Value for deposit/withdraw is restricted to positive values")

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            print("ERROR: Value for deposit/withdraw is restricted to positive values")
        
    def __str__(self):
        symbol = self.conversion_rates[self.currency][1]
        return f"Owner: {self.owner}\nBalance: {symbol}{self.balance:.2f}"
    
    def __eq__(self, other):
        a2_balance = round(other.balance * self.conversion_rates[other.currency][0], 2)
        return self.balance == a2_balance
    
    def __add__(self, other):
        a2_balance = round(other.balance * self.conversion_rates[other.currency][0], 2)
        return Account(self.owner, self._currency, self.balance + a2_balance)
    
    @property
    def currency(self):
        c=  self._currency
        return c
    
    @currency.setter
    def currency(self, cr):
        if cr not in self.conversion_rates:
            raise ValueError("ERROR: Unsupported currency type")
        self._balance = round(self.balance *  self.conversion_rates[ self._currency][0], 2)
        self._currency = cr #calling property
    