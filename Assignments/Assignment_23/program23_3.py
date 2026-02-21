"""
    Class Name   : NumbersClass
    Description     : Checks whether a number is prime or perfect
                      and displays its factors.
    Input           : Integer number
    Output          : Prime status, Perfect status, and factors
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        return self.SumFactors() == self.Value


# Creating multiple objects
Obj1 = Numbers()
Obj2 = Numbers()

print("\nFor Number 1")
print("Prime:", Obj1.ChkPrime())
Obj1.Factors()
print("Perfect:", Obj1.ChkPerfect())

print("\nFor Number 2")
print("Prime:", Obj2.ChkPrime())
Obj2.Factors()
print("Perfect:", Obj2.ChkPerfect())