"""
    Class Name   : CircleClass
    Description     : Calculates area and circumference of a circle
                      using instance and class variables.
    Input           : Radius of circle
    Output          : Radius, Area, and Circumference
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

class Circle:
    PI = 3.14   # Class variable

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius =", self.Radius)
        print("Area =", self.Area)
        print("Circumference =", self.Circumference)


# Creating multiple objects
Obj1 = Circle()
Obj2 = Circle()

print("\nFor Circle 1")
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

print("\nFor Circle 2")
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()