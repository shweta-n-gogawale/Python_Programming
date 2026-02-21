"""
    Function Name   : CompareFiles
    Description     : Compares contents of two files using
                      command line arguments.
    Input           : Two file names (command line)
    Output          : Success or Failure
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

import sys

def CompareFiles():
    if len(sys.argv) != 3:
        print("Usage: python program.py <file1> <file2>")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            if f1.read() == f2.read():
                print("Success")
            else:
                print("Failure")

    except FileNotFoundError:
        print("One or both files not found")


# Function call
CompareFiles()