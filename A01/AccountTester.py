from Account import Account
from Savings import Savings
from Chequing import Chequing
from Investment import Investment

class TestAccount:
    def __init__(self):
        pass

    def test_account(self):
        print("\n----------------Testing Account-----------------------------")
        account = Account("Darshan Gautam")
        account.deposit(1500)
        print(account)
        account.withdraw(500)
        print(account)

    def savings_account_test(self):
        print("\n----------------Testing Savings Account-----------------------------")
        savings = Savings("Darshan Gautam", interestRate=2)
        savings.deposit(100)
        print(savings)
        savings.applyInterest()
        print("After applying interest:", savings)

    def chequing_account_test(self):
        print("\n----------------Testing Chequing Account-----------------------------")
        chequing = Chequing("Darshan Gautam", fee=3, overdraftLimit=250)
        chequing.deposit(150)
        print(chequing)
        chequing.withdraw(100) 
        print("After withdrawal:", chequing)

    def investment_account_test(self):
        print("\n----------------Testing Investment Account-----------------------------")
        investment = Investment("Darshan Gautam", "CAD", 1000)
        investment.buy("JD", 2)
        print(investment)
        investment.sell("JD", 1)
        print("After selling stocks:", investment)
        investment.updateStockPrice("JD", 120)
        print("After updating stock price:", investment)

    def run_test(self):
        self.test_account()
        self.savings_account_test()
        self.chequing_account_test()
        self.investment_account_test()




tester = TestAccount()
tester.run_test()
