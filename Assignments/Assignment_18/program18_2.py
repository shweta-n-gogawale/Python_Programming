"""
    Function Name   : MaxList
    Description     : Accepts N numbers from user, stores them in list and returns maximum number.
    Input           : list
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def MaxList(lst):
    max_no = lst[0]
    for i in lst:
        if i > max_no:
            max_no = i
    return max_no

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

print("Maximum:", MaxList(lst))
