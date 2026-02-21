"""
    Function Name   : SearchWordInFile
    Description     : Checks whether a given word is present in a file.
    Input           : File name and word
    Output          : Displays whether word is found or not
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

def SearchWordInFile():
    fname = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        with open(fname, "r") as f:
            data = f.read()
            if word in data:
                print("Word", word, "is found in", fname)
            else:
                print("Word", word, "is not found in", fname)

    except FileNotFoundError:
        print("File not found")


# Function call
SearchWordInFile()