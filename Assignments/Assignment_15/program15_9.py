"""
    Function Name   : ProductAll
    Description     : Accepts a list of numbers and returns product of all elements.
    Input           : list
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-30
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a * b, numbers)
print(result)
