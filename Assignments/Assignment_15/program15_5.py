"""
    Function Name   : DisplayGrade
    Description     : Accepts marks and displays grade based on conditions.
    Input           : int
    Output          : Grade
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def DisplayGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

marks = int(input("Enter marks: "))
DisplayGrade(marks)
