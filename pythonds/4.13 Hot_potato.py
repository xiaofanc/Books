"""
Queue:
Hot potato

queue acts like a circle and counting continues back at the beginning until the value is reached. 
Our program will input a list of names and a constant, call it “num,” to be used for counting. It will return the name of the last person remaining after repetitive counting by num.

"""
from Queue import Queue

def hotpotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()

print(hotpotato(["Bill","David","Susan","Jane","Kent","Brad"], 7))