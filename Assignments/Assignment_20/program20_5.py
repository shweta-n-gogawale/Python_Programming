"""
    Function Name   : SequentialThreads
    Description     : Thread1 prints 1 to 50, Thread2 prints 50 to 1 after Thread1.
    Input           : None
    Output          : Numbers
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import threading

def Thread1():
    for i in range(1, 51):
        print("Thread1:", i)

def Thread2():
    for i in range(50, 0, -1):
        print("Thread2:", i)

t1 = threading.Thread(target=Thread1)
t2 = threading.Thread(target=Thread2)

t1.start()
t1.join()   # Ensure Thread2 starts after Thread1 completes

t2.start()
t2.join()
print("Exit from main")