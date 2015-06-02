import time
import threading
from random import random

numSent = 0
timer = threading.Event()
lock = threading.Condition()

def send():
    global numSent
    while numSent < 10:
        lock.acquire()
        print "Sending", numSent+1
        numSent += 1
        lock.wait(1)
        lock.release()

def read():
    lock.acquire()
    timer.wait(0.1)
    print "Reading"
    if random() > 0.5:
        lock.notify()
        lock.wait(random()/2)
    lock.release()

def receive():
    global numSent
    while numSent < 10:
        read()
    

receiveThread = threading.Thread(name="Thread-0", target=receive)
sendThread = threading.Thread(name="Thread-1", target=send)

receiveThread.start()
sendThread.start()
