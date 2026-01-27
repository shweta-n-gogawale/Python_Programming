"""
    Function Name   : CheckDivisible
    Description     : Checks whether the given number is divisible by 3 and 5.
    Input           : int
    Output          : Divisible / Not Divisible
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def CheckDivisible(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

num = int(input("Enter a number: "))
CheckDivisible(num)
