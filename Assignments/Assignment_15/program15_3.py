"""
    Function Name   : OddList
    Description     : Accepts a list of numbers and returns list of odd numbers.
    Input           : list
    Output          : list
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-30
"""

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)
