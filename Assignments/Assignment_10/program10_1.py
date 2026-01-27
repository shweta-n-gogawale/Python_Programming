"""
    Function Name   : DisplayTable
    Description     : Accepts one number and prints its multiplication table.
    Input           : int
    Output          : Multiplication table
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def DisplayTable(no):
    for i in range(1, 11):
        print(no * i)

num = int(input("Enter a number: "))
DisplayTable(num)