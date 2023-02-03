'''5. Create a bank account class that has attributes owner, balance and
 two methods deposit and withdraw. Withdrawals may not exceed the available balance. 
 Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposits(self,dep):
        self.balance += dep
    
    def withdrawal(self,wd):
        if wd > self.balance:
            print("Exceeds the balance!")
        else:
            self.balance -= wd
            print("Successfully withdrawn!")

b = account("BAtyrkhan", 25000)

b.deposits(300000)

print(b.balance)

b.withdrawal(4000000)