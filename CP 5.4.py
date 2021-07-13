class Bank:
    def __init__(self,account_money):
        self.account_money=account_money
        
    def deposit(self,deposit):
        self.deposit=deposit
        self.account_money=self.account_money+self.deposit
        return(self.account_money)

    def withdraw(self,withdraw):
        self.withdraw=withdraw
        self.account_money=self.account_money-self.withdraw
        return(self.account_money)
