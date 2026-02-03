"""
    Function Name   : PrimeDoubleMax
    Description     : Filters prime numbers, multiplies each by 2,
                      and returns maximum value.
    Input           : list
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

from functools import reduce

def IsPrime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

numbers = [2, 70, 11, 10, 17, 23, 31, 77]

filtered = list(filter(IsPrime, numbers))
mapped = list(map(lambda x: x * 2, filtered))
result = reduce(lambda a, b: a if a > b else b, mapped)

print("List after filter:", filtered)
print("List after map:", mapped)
print("Output of reduce:", result)
