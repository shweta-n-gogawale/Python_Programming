"""
    Function Name   : DisplayOdd
    Description     : Accepts one number and prints all odd numbers till that number.
    Input           : int
    Output          : Odd numbers
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def DisplayOdd(N):
    for i in range(1, N + 1, 2):
        print(i)

N = int(input("Enter a number: "))
DisplayOdd(N)