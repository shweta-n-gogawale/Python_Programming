"""
    Function Name   : ArithmeticOperations
    Description     : Accepts two numbers and performs addition, subtraction,
                      multiplication and division.
    Input           : int, int
    Output          : Arithmetic results
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def ArithmeticOperations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
ArithmeticOperations(num1, num2)
