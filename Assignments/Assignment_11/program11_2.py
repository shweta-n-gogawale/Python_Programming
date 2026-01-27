"""
    Function Name   : CountDigits
    Description     : Accepts one number and prints count of digits in that number.
    Input           : int
    Output          : Count of digits
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def CountDigits(no):
    count = 0
    while no > 0:
        no = no // 10
        count += 1
    print("Count of digits:", count)

num = int(input("Enter a number: "))
CountDigits(num)
