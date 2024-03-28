# import class Account from Account.py
from  Account import Account

class Savings(Account):
    def __init__(self, owner, interestRate, currency="CAD", balance=0):
        super().__init__(owner, currency, balance)
        self.interestRate = interestRate  

    @property
    def interestRate(self):
        return self._interestRate

    @interestRate.setter
    def interestRate(self, value):
        if value < 0:
            print("ERROR: Interest rate cannot be negative")
        else:
            self._interestRate = value
    

    def applyInterest(self):
        monthly_interest = self.balance * (self.interestRate / 100) / 12
        self.balance += monthly_interest

    def __str__(self):
        base_str = super().__str__()  
        interest_str = f"\nInterest Rate: {self.interestRate}%"
        return base_str + interest_str
