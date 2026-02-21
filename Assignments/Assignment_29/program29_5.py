"""
    Function Name   : FrequencyOfString
    Description     : Counts frequency of a given string in a file.
    Input           : File name and string
    Output          : Frequency of string in file
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

def FrequencyOfString():
    fname = input("Enter file name: ")
    word = input("Enter string to search: ")

    try:
        with open(fname, "r") as f:
            data = f.read()
            count = data.count(word)
            print("Frequency of", word, "is:", count)
    except FileNotFoundError:
        print("File not found")


# Function call
FrequencyOfString()