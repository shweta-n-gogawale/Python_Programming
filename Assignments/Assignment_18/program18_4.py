"""
    Function Name   : Frequency
    Description     : Accepts list and a number and returns frequency of that number.
    Input           : list, int
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def Frequency(lst, search):
    count = 0
    for i in lst:
        if i == search:
            count += 1
    return count

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

print("List:", lst)
search = int(input("Enter element to search: "))
print("Frequency:", Frequency(lst, search))
