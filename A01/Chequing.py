from Account import Account

#  creating class for chequing account
class Chequing(Account):
    def __init__(self, owner, fee, overdraftLimit, currency = "CAD", balance = 0,):
        super().__init__(owner, currency, balance)
        self.fee = fee

        if overdraftLimit > 0:
            self.overdraftLimit = overdraftLimit
        else:
            print("Overdraft limit should be positive")
            
        if(balance > overdraftLimit):
            print("ERROR: Overdraft limit has been exceeded")

    def withdraw(self, amount):
        if amount + self.fee <= self.balance + self.overdraftLimit:
            self.balance -= (amount + self.fee)
        else:
            print("ERROR: Withdrawal and fee exceed the overdraft limit")
    
    def __str__(self):
        base_str = super().__str__()
        fee_str = f"\nFee: {self.conversion_rates[self._currency][1]}{self.fee:.2f}"
        overdraft_str = f"\nOverdraft Limit: {self.conversion_rates[self._currency][1]}{self.overdraftLimit:.2f}"
        return base_str + fee_str + overdraft_str
    
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value

    @property
    def overdraftLimit(self):
        return self._overdraftLimit

    @overdraftLimit.setter
    def overdraftLimit(self, value):
        if self.balance <= value:
            self._overdraftLimit = value
        else:
            print("ERROR: Overdraft limit will be exceeded. Update abandoned!")





