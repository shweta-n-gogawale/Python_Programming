"""
    Function Name   : CheckFileExists
    Description     : Checks whether a given file exists in the current directory.
    Input           : File name
    Output          : Displays whether file exists or not
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

import os

def CheckFileExists():
    fname = input("Enter file name: ")

    if os.path.exists(fname):
        print(fname, "exists in current directory")
    else:
        print(fname, "does not exist in current directory")


# Function call
CheckFileExists()