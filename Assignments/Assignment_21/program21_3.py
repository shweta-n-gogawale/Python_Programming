"""
    Function Name   : SharedCounter
    Description     : Multiple threads increment shared counter using Lock.
    Input           : None
    Output          : Final counter value
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-03
"""

import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

t1 = threading.Thread(target=Increment)
t2 = threading.Thread(target=Increment)
t3 = threading.Thread(target=Increment)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Final Counter Value:", counter)
