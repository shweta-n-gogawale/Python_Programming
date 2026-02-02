"""
    Function Name   : DisplayStar
    Description     : Accepts a number and prints that many '*' on screen.
    Input           : int
    Output          : *
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-02
"""

def DisplayStar(no):
    for _ in range(no):
        print("*", end=" ")

num = int(input("Enter number: "))
DisplayStar(num)
