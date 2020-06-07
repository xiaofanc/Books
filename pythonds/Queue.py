"""

Queue is an ordered collection of items which are added at one end, called the “rear,” and removed from the other end, called the “front.”

Queue()
enqueue(item): add to the rear
dequeue(): pop from front
isEmpty()
size()

"""
# Implementing a Stack class using Python lists. Rear is list[0], and front is list[-1], so that enqueue is O(n), and dequeue is O(1)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
        
    def __repr__(self):
        return "%s" % (self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(3)
    print(q.size())
