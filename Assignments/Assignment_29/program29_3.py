"""
    Function Name   : CopyFileContents
    Description     : Copies contents of an existing file into a new file
                      named Demo.txt using command line arguments.
    Input           : Source file name (command line)
    Output          : Creates Demo.txt and copies contents
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

import sys

def CopyFileContents():
    if len(sys.argv) != 2:
        print("Usage: python program.py <source_file>")
        return

    src = sys.argv[1]

    try:
        with open(src, "r") as fsrc:
            data = fsrc.read()

        with open("Demo.txt", "w") as fdst:
            fdst.write(data)

        print("Contents copied to Demo.txt successfully")

    except FileNotFoundError:
        print("Source file not found")


# Function call
CopyFileContents()