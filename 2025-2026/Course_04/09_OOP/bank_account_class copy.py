# -*- coding: utf-8  -*-
from datetime import datetime
CREDIT_INTEREST_RATE = 0.04     # 4% creditor interest rate
DEBIT_INTEREST_RATE = 0.05      # 5% debit interest rate

class bank_account:
    def __init__(self, account_number:int, account_name:str, 
                 creation_date: datetime, balance = 0.00, is_debit_authorized= False, 
                 is_credit_authorized= True, locked=False, ):
        self.number = account_number
        self.name = account_name
        self.creation_date = creation_date
        self.balance = balance
        self.is_debit_authorized = is_debit_authorized
        self.is_credit_authorized = is_credit_authorized
        self.locked = locked



    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            if not self.is_debit_authorized:
                print("Insufficient balance")
        else :
            self.balance -= amount

    def agios(self):
        self.balance *= (1 - DEBIT_INTEREST_RATE)

    def interests(self):
        self.balance *= (1 + CREDIT_INTEREST_RATE)

    def __str__(self):
        return f"Account {self.number}: {self.name}, Balance: {self.balance}"
    
Account_0001 = bank_account(30, "Stock", datetime.now(), 50, True, True, False)


    
# print(Account_0001)

print("le numéro de compte est : ", Account_0001.number)
print("le nom du compte est : ", Account_0001.name)
print("le solde : ", Account_0001.balance)

Account_0001.deposit(100)
print("le solde : ", Account_0001.balance)
Account_0001.withdraw(110)
print("le solde : ", Account_0001.balance)
Account_0001.agios()
print("le solde : ", Account_0001.balance)
Account_0001.interests()
print("le solde : ", Account_0001.balance)
Account_0001.creation_date=datetime.now()

