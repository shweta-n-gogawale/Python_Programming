"""
    Function Name   : CheckPrime
    Description     : Checks whether a number is prime or not.
    Input           : int
    Output          : Prime / Not Prime
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

def CheckPrime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime Number"

num = int(input("Enter number: "))
print(CheckPrime(num))
