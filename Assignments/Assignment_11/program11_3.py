"""
    Function Name   : SumDigits
    Description     : Accepts one number and prints sum of its digits.
    Input           : int
    Output          : Sum of digits
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""
def SumDigits(no):
    total = 0
    while no > 0:
        total += no % 10
        no //= 10
    print("Sum of digits:", total)

num = int(input("Enter a number: "))
SumDigits(num)