"""
In order to implement an unordered list, we will construct what is commonly known as a linked list. 

List()
add(item)      - O(1) !!
remove(item)   - O(n)
search(item)   - O(n)
isEmpty()      - O(1)
size()         - O(n)
append(item)
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

    # always add the new node to the beginning of the linked list
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # based on linked list traversal
    def size(self):
        n = 0
        cur = self.head
        while cur != None: # current reference
            cur = cur.getNext()
            n += 1
        return n

    def search(self, item):
        found = False
        cur = self.head
        while cur != None and not found:
            if cur.getData() == item:
                found = True
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





