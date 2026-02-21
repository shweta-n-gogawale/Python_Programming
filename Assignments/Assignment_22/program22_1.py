"""
    Class Name   : DemoClass
    Description     : Demonstrates use of instance variables, class variable,
                      constructor, and instance methods.
    Input           : Two integers
    Output          : Displays values of instance variables
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

class Demo:
    Value = 0   # Class variable

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Fun Method:")
        print("No1 =", self.no1)
        print("No2 =", self.no2)

    def Gun(self):
        print("Gun Method:")
        print("No1 =", self.no1)
        print("No2 =", self.no2)


# Creating objects
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Calling methods in given sequence
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()