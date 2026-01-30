"""
    Function Name   : SquareList
    Description     : Accepts a list of numbers and returns list of squares.
    Input           : list
    Output          : list
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-30
"""

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print(result)
