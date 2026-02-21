"""
    Class Name   : BankAccountClass
    Description     : Simulates bank account operations like deposit,
                      withdrawal, and interest calculation.
    Input           : Account holder name and amounts
    Output          : Displays account details and interest
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

class BankAccount:
    ROI = 10.5   # Class variable

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        amt = float(input("Enter deposit amount: "))
        self.Amount += amt

    def Withdraw(self):
        amt = float(input("Enter withdrawal amount: "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


# Creating multiple objects
Obj1 = BankAccount("Shweta", 5000)
Obj2 = BankAccount("Aathvan", 8000)

print("\nAccount 1")
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest:", Obj1.CalculateInterest())

print("\nAccount 2")
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest:", Obj2.CalculateInterest())