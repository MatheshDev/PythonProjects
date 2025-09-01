class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self,amount):
        if(amount < 0):
            print("Return a amount greater than 1")
        else:
            self.balance += amount
            print("Amount Deposited : ",amount,". Current Balance : ",self.balance)
    def withdraw(self,amount):
        if(amount <= self.balance):
            print("Insufficient Balance")
        else:
            self.balance -= amount
    def display(self):
        print("Account Number : ", self.account_number)
        print("holder_name : ",self.holder_name)
        print("Balance : ", self.balance)
    

Accounts = [BankAccount(123456789,"Maddy",1000),BankAccount(987654321,"Vicky",2000)]

Accounts[1].display()