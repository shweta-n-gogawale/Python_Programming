"""
    Function Name   : CountWordsInFile
    Description     : Counts total number of words present in a file.
    Input           : File name
    Output          : Total number of words in file
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

def CountWordsInFile():
    fname = input("Enter file name: ")

    try:
        with open(fname, "r") as f:
            data = f.read()
            words = data.split()
            print("Total number of words:", len(words))

    except FileNotFoundError:
        print("File not found")


# Function call
CountWordsInFile()