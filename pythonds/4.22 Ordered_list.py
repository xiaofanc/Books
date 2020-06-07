"""
For example, if the list of integers shown above were an ordered list (ascending order), then it could be written as 17, 26, 31, 54, 77, and 93. 

OrderedList()
add(item)      - O(n) !!
remove(item)   - O(n)
search(item)   - O(n)
isEmpty()      - O(1)
size()         - O(n)
index(item)
insert(pos,item)
pop()
pop(pos)

"""
# the Node Class
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# The Unordered List Class
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # needs modification
    # Assume we have the ordered list consisting of 17, 26, 54, 77, and 93 and we want to add the value 31.
    def add(self, item):
        prev, cur = None, self.head
        found = False
        # find the first number > 31
        while cur != None and not found:
            if cur.getData() < item:
                prev, cur = cur, cur.getNext()
            else: 
                found = True

        # cur is the position to add
        temp = Node(item)
        if prev == None: # add before head
            temp.setNext(self.head)
            self.head = temp  # new head
        else:
            temp.setNext(cur)
            prev.setNext(temp)

    # based on linked list traversal
    def size(self):
        n = 0
        cur = self.head
        while cur != None: # current reference
            cur = cur.getNext()
            n += 1
        return n

    # needs modification
    # in the case where the item is not in the list, we can take advantage of the ordering to stop the search as soon as possible.
    def search(self, item):
        found = False
        cur = self.head
        while cur != None and not found:
            if cur.getData() == item:
                found = True
            elif cur.getNext() > item:
                return found # False
            else:
                cur = cur.getNext()

        return found

    # assume that item is present
    def remove(self, item):
        prev, cur = None, self.head
        found = False
        while not found:
            if cur.getData() == item:
                found = True
            else:
                prev, cur = cur, cur.getNext()

        if prev == None: # remove head
            self.head = cur.getNext()
        else:
            prev.setNext(cur.getNext())

    def printNode(self):
        cur = self.head
        while cur:
            print(cur.getData(), "-->")
            cur = cur.getNext()
        print("None")

if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    mylist.printNode()
    print(mylist.search(17))
    mylist.remove(17)
    mylist.printNode()