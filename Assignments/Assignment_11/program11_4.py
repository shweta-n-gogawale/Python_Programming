"""
    Function Name   : ReverseNumber
    Description     : Accepts one number and prints reverse of that number.
    Input           : int
    Output          : Reversed number
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def ReverseNumber(no):
    rev = 0
    while no > 0:
        rev = rev * 10 + (no % 10)
        no //= 10
    print(rev)

num = int(input("Enter a number: "))
ReverseNumber(num)
