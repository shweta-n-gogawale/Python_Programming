"""
    Function Name   : MinList
    Description     : Accepts N numbers from user, stores them in list and returns minimum number.
    Input           : list
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def MinList(lst):
    min_no = lst[0]
    for i in lst:
        if i < min_no:
            min_no = i
    return min_no

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

print("Minimum:", MinList(lst))
