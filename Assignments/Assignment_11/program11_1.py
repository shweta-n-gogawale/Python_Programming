"""
    Function Name   : CheckPrime
    Description     : Accepts one number and checks whether it is prime or not.
    Input           : int
    Output          : Prime Number / Not Prime
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""
def CheckPrime(no):
    if no <= 1:
        print(f"{no} is Not Prime")
        return
    for i in range(2, no):
        if no % i == 0:
            print(f"{no} is Not Prime")
            return
    print(f"{no} is Prime")
num = int(input("Enter a number: "))
CheckPrime(num)