#Bank

import random
import datetime

class BankAccount:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin 
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.transaction_history = []


    def generate_account_number(self):
        return random.randint(10000000, 99999999)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction_id =self.generate_transaction_id()
            self.transaction_history.append((transaction_id, datetime.datetime.now(), 'Deposit', amount))
            print(f"{amount} deposited successfully.Transaction id:{transaction_id}")
        else:
            print("Deposit amount must be greater than zero")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            transaction_id = self.generate_transaction_id()
            self.transaction_history.append((transaction_id, datetime.datetime.now(), 'Withdrawl', amount))
            print(f"{amount} withdrwan successfully. Transaction id:{transaction_id} ")
        else:
            print("Insufficient Funds.")


    def get_balance(self):
        print(f"Your Balance is {self.balance}")


    def print_transaction_history(self):
        print("Transaction History:")
        for transaction_id, date, action, amount in self.transaction_history:
            print(f"Transaction id:{transaction_id} - {date} - {action} - {amount}")

        
    def generate_transaction_id(self):
        return random.randint(100000,999999)
    
if __name__ == "__main__":
    print("Welcome To Our Bank!")

    #create new account
    account_name = input("Enter Your Name:")
    account_pin = input("Set Your 4-Digit pin:")
    account = BankAccount(account_name, account_pin)

    while True:
        print('\nWhat could you like to do ?\n')
        print('1.Deposit')
        print('2.Withdraw')
        print('3.Check Balance')
        print('4.View Transaction History')
        print('5.Exit')


        choice = input("Enter Your Choice (1-5):")

        if choice == '1':
            amount = float(input("Enter Amount to Deposit:"))
            account.deposit(amount)
        
        elif choice == '2':
            amount == float(input("Enter Amount to Withdraw:"))
            account.withdraw(amount)

        elif choice == '3':
            account.get_balance()

        elif choice == '4':
            account.print_transaction_history()

        elif choice == '5':
            print("Thank You for Banking With Us")
            break
        else:
            print("Invalid Choice.Please enter a number from 1 to 5.")


