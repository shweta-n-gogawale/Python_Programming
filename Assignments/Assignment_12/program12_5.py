"""
    Function Name   : DisplayReverse
    Description     : Accepts one number and prints numbers in reverse order.
    Input           : int
    Output          : Numbers from N to 1
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def DisplayReverse(no):
    for i in range(no, 0, -1):
        print(i) 

num = int(input("Enter a number: "))
DisplayReverse(num)
