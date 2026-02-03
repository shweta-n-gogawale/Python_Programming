"""
    Function Name   : DisplayPattern
    Description     : Displays 5x5 star pattern.
    Input           : int
    Output          : Star pattern
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def DisplayPattern(n):
    for _ in range(n):
        print("* " * n)

num = int(input("Enter number: "))
DisplayPattern(num)
