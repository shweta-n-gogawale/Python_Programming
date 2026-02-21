"""
    Function Name   : CountLinesInFile
    Description     : Counts total number of lines present in a file.
    Input           : File name
    Output          : Total number of lines in file
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

def CountLinesInFile():
    fname = input("Enter file name: ")

    try:
        with open(fname, "r") as f:
            count = 0
            for line in f:
                count += 1
        print("Total number of lines:", count)

    except FileNotFoundError:
        print("File not found")


# Function call
CountLinesInFile()