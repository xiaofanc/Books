"""
linear data structure: Stacks, queues, deques, and lists
stack:
A stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This end is commonly referred to as the “top.” The end opposite the top is known as the “base.”

Stack()
push(item): add to the top
pop(): the top
peek(): the top
isEmpty()
size()
"""
# Implementing a Stack class using Python lists

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# implement the stack using a list where the top is at the beginning instead of at the end.
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

s = Stack()
s.push('hello')
s.push('true')
print(s.pop())






