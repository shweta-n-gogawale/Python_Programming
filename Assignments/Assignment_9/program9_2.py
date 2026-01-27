"""
    Function Name   : ChkGreater
    Description     : Accepts two numbers and prints the greater number.
    Input           : int, int
    Output          : Prints greater number
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def ChkGreater(no1, no2):
    if no1 > no2:
        print(f"{no1} is greater")
    else:
        print(f"{no2} is greater")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
ChkGreater(a, b)