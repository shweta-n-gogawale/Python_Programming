"""
    Function Name   : EvenOddFactor
    Description     : Displays even and odd factors and their sum using threads.
    Input           : int
    Output          : Sum of even and odd factors
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import threading

def EvenFactor(no):
    total = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print("Even Factor:", i)
            total += i
    print("Sum of Even Factors:", total)

def OddFactor(no):
    total = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print("Odd Factor:", i)
            total += i
    print("Sum of Odd Factors:", total)

num = int(input("Enter number: "))

t1 = threading.Thread(target=EvenFactor, args=(num,))
t2 = threading.Thread(target=OddFactor, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
