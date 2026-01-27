"""
    Function Name   : DisplayNumbers
    Description     : Accepts one number and prints numbers from 1 to that number.
    Input           : int
    Output          : Numbers from 1 to N
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def DisplayNumbers(no):
    for i in range(1, no + 1):
        print(i)

num = int(input("Enter a number: "))
DisplayNumbers(num)
