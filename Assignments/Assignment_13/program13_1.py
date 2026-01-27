"""
    Function Name   : AreaRectangle
    Description     : Accepts length and width of rectangle and prints its area.
    Input           : int, int
    Output          : Area of rectangle
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def AreaRectangle(length, width):
    area = length * width
    print("Area of rectangle:", area)

l = int(input("Enter length: "))
w = int(input("Enter width: "))
AreaRectangle(l, w)