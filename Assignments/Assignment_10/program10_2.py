"""
    Function Name   : Factorial
    Description     : Accepts one number and prints factorial of that number.
    Input           : int
    Output          : Factorial of number
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def Factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    print("Factorial of", no, "is:", fact)

no = int(input("Enter a number: "))
Factorial(no)