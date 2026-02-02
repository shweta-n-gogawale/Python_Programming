"""
    Function Name   : CheckDivisible
    Description     : Accepts a number and returns True if divisible by 5 otherwise False.
    Input           : int
    Output          : Boolean
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-02
"""

def CheckDivisible(no):
    return no % 5 == 0

num = int(input("Enter number: "))
print(CheckDivisible(num))
