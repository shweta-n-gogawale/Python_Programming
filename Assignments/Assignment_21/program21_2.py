"""
    Function Name   : MaxMinThread
    Description     : Finds maximum and minimum element from list using threads.
    Input           : list
    Output          : Maximum and Minimum value
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import threading

def Maximum(lst):
    print("Maximum element:", max(lst))

def Minimum(lst):
    print("Minimum element:", min(lst))

lst = []
n = int(input("Enter number of elements: "))

for _ in range(n):
    lst.append(int(input("Enter element: ")))

t1 = threading.Thread(target=Maximum, args=(lst,))
t2 = threading.Thread(target=Minimum, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()
print("Main thread execution completed.")