"""
    Function Name   : DivBy3And5
    Description     : Accepts a list of numbers and returns numbers divisible by both 3 and 5.
    Input           : list
    Output          : list
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-30
"""

numbers = [10, 15, 20, 30, 45, 50]
result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print(result)
