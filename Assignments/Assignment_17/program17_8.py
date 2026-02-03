"""
    Function Name   : IncrementPattern
    Description     : Displays incremental number pattern.
    Input           : int
    Output          : Pattern
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def IncrementPattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

num = int(input("Enter number: "))
IncrementPattern(num)
