"""
    Function Name   : AddList
    Description     : Accepts N numbers from user, stores them in list and returns addition of all elements.
    Input           : list
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def AddList(lst):
    total = 0
    for i in lst:
        total += i
    return total

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

print("Addition:", AddList(lst))
