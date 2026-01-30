"""
    Function Name   : CheckPerfect
    Description     : Accepts one number and checks whether it is a perfect number.
    Input           : int
    Output          : Perfect Number / Not Perfect
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def CheckPerfect(no):
    total = 0
    for i in range(1, no):
        if no % i == 0:
            total += i

    if total == no:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

num = int(input("Enter a number: "))
CheckPerfect(num)