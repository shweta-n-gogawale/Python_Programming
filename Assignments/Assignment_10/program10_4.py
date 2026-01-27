"""
    Function Name   : DisplayEven
    Description     : Accepts one number and prints all even numbers till that number.
    Input           : int
    Output          : Even numbers
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""
def DisplayEven(N):
    for i in range(2, N + 1, 2):
        print(i)

N = int(input("Enter a number: "))
DisplayEven(N)