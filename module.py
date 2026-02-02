# module.py

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def greet(self):
        print(f"Welcome, {self.owner}! Your balance is ${self.balance}.")

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
          self.balance = self.balance - amount
        else: 
            print("insufficientfunds. withdrawal canceled")
        
    
