"""
    Function Name   : EvenOddList
    Description     : Extracts even and odd elements from list and displays their sum.
    Input           : list
    Output          : Sum of even and odd elements
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import threading

def EvenList(lst):
    total = 0
    for i in lst:
        if i % 2 == 0:
            print("Even:", i)
            total += i
    print("Sum of Even Elements:", total)

def OddList(lst):
    total = 0
    for i in lst:
        if i % 2 != 0:
            print("Odd:", i)
            total += i
    print("Sum of Odd Elements:", total)

lst = [10, 15, 20, 25, 30, 35]

t1 = threading.Thread(target=EvenList, args=(lst,))
t2 = threading.Thread(target=OddList, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()
