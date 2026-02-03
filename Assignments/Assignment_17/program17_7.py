"""
    Function Name   : DisplayNumberPattern
    Description     : Displays number pattern from 1 to N.
    Input           : int
    Output          : Number pattern
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def DisplayNumberPattern(n):
    for _ in range(n):
        for i in range(1, n + 1):
            print(i, end=" ")
        print()

num = int(input("Enter number: "))
DisplayNumberPattern(num)
