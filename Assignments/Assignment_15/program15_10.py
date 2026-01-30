"""
    Function Name   : CountEven
    Description     : Accepts a list of numbers and returns count of even numbers.
    Input           : list
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-30
"""

numbers = [1, 2, 3, 4, 5, 6, 8]
result = len(list(filter(lambda x: x % 2 == 0, numbers)))
print(result)
