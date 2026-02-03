"""
    Function Name   : SumProductThread
    Description     : Computes sum and product of list elements using threads.
    Input           : list
    Output          : Sum and Product
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import threading
from functools import reduce

def SumList(lst):
    print("Sum of elements:", sum(lst))

def ProductList(lst):
    product = reduce(lambda a, b: a * b, lst)
    print("Product of elements:", product)

lst = []
n = int(input("Enter number of elements: "))

for _ in range(n):
    lst.append(int(input("Enter element: ")))

t1 = threading.Thread(target=SumList, args=(lst,))
t2 = threading.Thread(target=ProductList, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()
print("Main thread execution completed.")