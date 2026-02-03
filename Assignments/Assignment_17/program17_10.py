"""
    Function Name   : SumDigits
    Description     : Returns sum of digits of a number.
    Input           : int
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def SumDigits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter number: "))
print(SumDigits(num))
