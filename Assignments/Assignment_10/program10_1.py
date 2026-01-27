"""
    Function Name   : Display
    Description     : Prints "Jay Ganesh" on console.
    Input           : None
    Output          : Jay Ganesh
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def DisplayTable(no):
    for i in range(1, 11):
        print(no * i)

num = int(input("Enter a number: "))
DisplayTable(num)