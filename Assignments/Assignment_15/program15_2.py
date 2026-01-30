"""
    Function Name   : AreaCircle
    Description     : Accepts radius of circle and prints its area.
    Input           : int
    Output          : Area of circle
    Author          : Shweta Narayan Gogawale
    Date            : 2026-01-27
"""

def AreaCircle(radius):
    area = 3.14 * radius * radius
    print("Area of circle:", area)

r = int(input("Enter radius: "))
AreaCircle(r)
