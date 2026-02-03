"""
    Function Name   : PrimeNonPrime
    Description     : Creates two threads to display prime and non-prime numbers from list.
    Input           : list
    Output          : Prime and Non-prime numbers
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import threading

def IsPrime(no):
    if no <= 1:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def Prime(lst):
    print("Prime Numbers:")
    for i in lst:
        if IsPrime(i):
            print(i)

def NonPrime(lst):
    print("Non-Prime Numbers:")
    for i in lst:
        if not IsPrime(i):
            print(i)

lst = [10, 11, 12, 13, 14, 15, 17, 19]

t1 = threading.Thread(target=Prime, args=(lst,))
t2 = threading.Thread(target=NonPrime, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()
print("Exit from main") 