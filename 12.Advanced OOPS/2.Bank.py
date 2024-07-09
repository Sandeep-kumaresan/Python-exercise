class Bank:
    def __init__(self):
        self.customers={}
    def account(self,acc,amt=0):
        if acc in self.customers:
            return "Account already exist"
        else:
            self.customers[acc]=amt
            return "Account created successfully"
    def deposit(self,acc,amt):
        if acc in self.customers:
            self.customers[acc]+=amt
            return "Amount deposited"
        else:
            return "Account doesn't exist"
    def withdraw(self,acc,amt):
        if acc in self.customers:
            if self.customers[acc]>=amt:
                self.customers[acc]-=amt
                return "Amount withdrawal success"
            else:
                return "Insufficient funds"
        else:
            return "Account doesn't exist"
    def balance(self,acc):
        if acc in self.customers:
            print(self.customers[acc])
        else:
            return "Account doesn't exist"
bank=Bank()
bank.account(1)
bank.account(22)
bank.account(35)
bank.deposit(1,200)
bank.deposit(22,500)
bank.deposit(35,1000)
bank.withdraw(35,500)
bank.withdraw(22,35)
bank.withdraw(1,25)
bank.balance(1)
bank.balance(22)
bank.balance(35)




