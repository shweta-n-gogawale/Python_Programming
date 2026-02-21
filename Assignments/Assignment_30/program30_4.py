"""
    Function Name   : CopyFileContents
    Description     : Copies contents from an existing file into a new file.
    Input           : Source file and destination file names
    Output          : Copies contents successfully
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

def CopyFileContents():
    src = input("Enter source file name: ")
    dest = input("Enter destination file name: ")

    try:
        with open(src, "r") as fsrc:
            data = fsrc.read()

        with open(dest, "w") as fdest:
            fdest.write(data)

        print("Contents of", src, "copied into", dest)

    except FileNotFoundError:
        print("Source file not found")


# Function call
CopyFileContents()