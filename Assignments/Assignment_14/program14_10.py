"""
    Function Name   : Largest
    Description     : Accepts three numbers and returns largest number.
    Input           : int, int, int
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-30
"""

Largest = lambda a, b, c: a if a > b and a > c else (b if b > c else c)
print(Largest(10, 25, 15))
