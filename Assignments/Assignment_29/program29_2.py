"""
    Function Name   : DisplayFileContents
    Description     : Opens a file and displays its entire contents
                      on the console.
    Input           : File name
    Output          : Displays file contents
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

def DisplayFileContents():
    fname = input("Enter file name: ")

    try:
        with open(fname, "r") as f:
            data = f.read()
            print("\nFile Contents:\n")
            print(data)
    except FileNotFoundError:
        print("File not found")


# Function call
DisplayFileContents()