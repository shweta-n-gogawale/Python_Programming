"""
    Function Name   : ListPrime
    Description     : Accepts list of numbers and returns addition of all prime numbers.
    Input           : list
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import MarvellousNum

def ListPrime(lst):
    total = 0
    for i in lst:
        if MarvellousNum.ChkPrime(i):
            total += i
    return total

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

print("Addition of prime numbers:", ListPrime(lst))
