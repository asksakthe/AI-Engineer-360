class BankAccount:
    
    def __init__(self,account_holder, balance, acc_type):
        self.account_holder = account_holder
        self.balance = float(balance)
        self.acc_type = acc_type
        
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.amount + self.balance
        return f"{self.balance} updated into your account"
       
       
    def Withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= self.amount
            print(f"amount Rs.{self.amount} is withdrawn from your account. current balance is {self.balance}")
    
    def display_balance(self, amount):
        return f"Bank Account Details :- \n------------------------ \n \tAccount Name: {self.account_holder} \n \tAccount Type : {self.acc_type} \n \tCurrent Balance: {self.balance}"
        
        


if __name__ == "__main__":
    print("Account Details")
        
        