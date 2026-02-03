"""
    Function Name   : SumOfFactors
    Description     : Returns addition of factors of a number.
    Input           : int
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def SumOfFactors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

num = int(input("Enter number: "))
print(SumOfFactors(num))
