"""
    Function Name   : DisplayStarPattern
    Description     : Displays vertical star pattern.
    Input           : int
    Output          : Star pattern
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def DisplayStarPattern(n):
    for _ in range(n):
        print("*")

num = int(input("Enter number: "))
DisplayStarPattern(num)
