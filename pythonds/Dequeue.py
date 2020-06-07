"""

A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front and a rear, and the items remain positioned in the collection.

New items can be added at either the front or the rear. Likewise, existing items can be removed from either end.

In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure.

Deque()
addFront(item)
addRear(item)
removeFront()
removeRear()
isEmpty()
size()

"""
# assume that the rear of the deque is at position 0 in the list.
# adding and removing items from the front is O(1)
# adding and removing items from the rear is O(n)

class Deque():
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __repr__(self):
        return f"{self.items}"

if __name__ == '__main__':
    d = Deque()
    d.addRear(4)
    d.addFront('dog')
    d.addRear('cat')
    d.addRear(True)
    print(d)



