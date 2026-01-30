"""
    Function Name   : MinElement
    Description     : Accepts a list of numbers and returns minimum element.
    Input           : list
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-30
"""

from functools import reduce

numbers = [10, 25, 5, 40, 15]
result = reduce(lambda a, b: a if a < b else b, numbers)
print(result)
