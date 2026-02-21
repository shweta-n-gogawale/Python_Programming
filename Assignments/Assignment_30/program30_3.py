"""
    Function Name   : DisplayFileLineByLine
    Description     : Displays contents of a file line by line on screen.
    Input           : File name
    Output          : Displays each line of file one by one
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

def DisplayFileLineByLine():
    fname = input("Enter file name: ")

    try:
        with open(fname, "r") as f:
            for line in f:
                print(line)

    except FileNotFoundError:
        print("File not found")


# Function call
DisplayFileLineByLine()