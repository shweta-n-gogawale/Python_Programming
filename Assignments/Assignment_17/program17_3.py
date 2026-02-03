"""
    Function Name   : Factorial
    Description     : Returns factorial of a number.
    Input           : int
    Output          : int
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter number: "))
print(Factorial(num))
