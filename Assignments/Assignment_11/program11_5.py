"""
    Function Name   : CheckPalindrome
    Description     : Accepts one number and checks whether it is palindrome or not.
    Input           : int
    Output          : Palindrome / Not Palindrome
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def CheckPalindrome(no):
    temp = no
    rev = 0

    while no > 0:
        rev = rev * 10 + (no % 10)
        no //= 10

    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

num = int(input("Enter a number: "))
CheckPalindrome(num)
