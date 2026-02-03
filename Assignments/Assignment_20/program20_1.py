"""
    Function Name   : EvenOddThreads
    Description     : Creates two threads to display first 10 even and odd numbers.
    Input           : None
    Output          : Even and Odd numbers
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import threading

def Even():
    for i in range(1, 21):
        if i % 2 == 0:
            print("Even:", i)

def Odd():
    for i in range(1, 21):
        if i % 2 != 0:
            print("Odd:", i)

t1 = threading.Thread(target=Even)
t2 = threading.Thread(target=Odd)

t1.start()
t2.start()

t1.join()
t2.join()
