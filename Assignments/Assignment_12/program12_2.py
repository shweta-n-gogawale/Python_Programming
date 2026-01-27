"""
    Function Name   : DisplayFactors
    Description     : Accepts one number and prints its factors.
    Input           : int
    Output          : Factors of number
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def DisplayFactors(no):
    for i in range(1, no + 1):
        if no % i == 0:
            print(i)

num = int(input("Enter a number: "))
DisplayFactors(num)
