"""
    Function Name   : DisplayBinary
    Description     : Accepts one number and prints its binary equivalent.
    Input           : int
    Output          : Binary number
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def DisplayBinary(no):
    print("Binary equivalent:", bin(no)[2:]) # [2:] Removes '0b' prefix

num = int(input("Enter a number: "))
DisplayBinary(num)

