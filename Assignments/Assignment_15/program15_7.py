"""
    Function Name   : LongStrings
    Description     : Accepts a list of strings and returns strings with length greater than 5.
    Input           : list
    Output          : list
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-30
"""

strings = ["Python", "Java", "C", "Machine", "Learning"]
result = list(filter(lambda x: len(x) > 5, strings))
print(result)
