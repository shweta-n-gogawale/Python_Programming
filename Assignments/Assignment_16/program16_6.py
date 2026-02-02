"""
    Function Name   : CheckNumber
    Description     : Accepts a number and checks whether it is positive, negative or zero.
    Input           : int
    Output          : Positive / Negative / Zero
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-02
"""

def CheckNumber(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

num = int(input("Enter number: "))
CheckNumber(num)
