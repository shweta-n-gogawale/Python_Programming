"""
    Function Name   : CheckVowel
    Description     : Accepts one character and checks whether it is vowel or consonant.
    Input           : char
    Output          : Vowel / Consonant
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def CheckVowel(ch):
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")

ch = input("Enter a character: ")
CheckVowel(ch)
