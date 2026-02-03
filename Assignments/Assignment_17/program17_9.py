"""
    Function Name   : CountDigits
    Description     : Returns number of digits in a number.
    Input           : int
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def CountDigits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

num = int(input("Enter number: "))
print(CountDigits(num))
