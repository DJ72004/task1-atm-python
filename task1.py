# task1-atm-python# importing important modules
import random 
import numpy

class Account:
    depositFrequency = 4
    transactionMax = 40000
   # Construct an Account object. Mde to
    def _init_(self, id, balance = 0, withdrawalDailyMax = 50000,
    withdrawalFrequency=3,withdrwalTransactionMax=20000, depoDailyMax = 150000, 
    depositFrequency = 4, depoTransactionMax = 40000):
        self.id = id
        self.balance = balance
        # withdral
        self.withdrawalDailyMax = withdrawalDailyMax
        self.withdrawalFrequency=withdrawalFrequency
        self.withdrwalTransactionMax=withdrwalTransactionMax
        # deposit
        self.depoDailyMax=depoDailyMax
        self.depositFrequency = depositFrequency
        self.depoTransactionMax=depoTransactionMax

    def getId(self):
        return self.id
#  a function to get balance
    def getBalance(self):
        return self.balance
        # getters for withdrwal 
    def getWithdrawalFrequency(self):
        return self.withdrawalFrequency
    def getWithdrwalTransactionMax(self):
        return self. withdrwalTransactionMax
    def getWithdrawalDailyMax(self):
        return self.withdrawalDailyMax
# getters for depo
    def getDepoDailyMax(self):
        return self.depoDailyMax
    def getDepositFrequency(self):
        return self.depositFrequency
    def getDepoTransactionMax(self):
        return self.depoTransactionMax

#  a function to withdraw
    def withdraw(self, amount):
    #    here if you withdraw your new balance changes
        self.balance -= amount
#  a function to depoit
    def deposit(self, amount):
    #    deposit equals amount being deposited+existing balance
        self.balance += amount 

#  a function to quit coming later

def main():
    # Creating accounts 
    accounts = []
    for i in range(1000, 9999): 
        account = Account(i, 0)
        accounts.append(account)    
    # ATM Processes
    while True:
       # Reading id from user which represents a secret pin for security
        id = int(input("\n Please Enter Your account pin: "))
       # Loop till id is valid between 1000 and 9999 in a randomised manner(where the Random module come in)
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Pin.. Re-enter your Pin please: "))

        # while the pin is right(Id is pin here)
        while True:
            # Printing menu
            print("\n1 - Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Quit ")

            # Reading selection
            selection = int(input("\nEnter your selection: "))
            # Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getId() == id:
                    accountObj = acc
                    break
                   # View Balance
            if selection == 1:
               # Printing balance
                print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
             # Withdraw
            elif selection == 2:
                print("Your Balance is:" + str(accountObj.getBalance()))
               # Reading amount
                amt = float(input("\nPlease Enter amount to withdraw: "))
                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
    
                if ver_withdraw == "Yes":
                    print("Verify withdraw")
                else:
                    break

                if amt < accountObj.getBalance():
                    print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
                    # Calling withdraw method
                    accountObj.withdraw(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                    print("you have only 2 withdrawal times remain…
