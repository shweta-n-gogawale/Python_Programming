"""
    Function Name   : ChkNum
    Description     : Accepts one number and displays whether it is even or odd.
    Input           : int
    Output          : Even Number / Odd Number
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-02
"""

def ChkNum(no):
    if no % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

num = int(input("Enter number: "))
ChkNum(num)
