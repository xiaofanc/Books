"""
binary heap:
A binary heap will allow us both enqueue and dequeue items in 𝑂(log𝑛).

BinaryHeap() creates a new, empty, binary heap.
insert(k) adds a new item to the heap.
findMin() returns the item with the minimum key value, leaving item in the heap.
delMin() returns the item with the minimum key value, removing the item from the heap.
isEmpty() returns true if the heap is empty, false otherwise.
size() returns the number of items in the heap.
buildHeap(list) builds a new heap from a list of keys.

"""
# build a minheap
# In our heap implementation we keep the tree balanced by creating a complete binary tree. 
# In a minheap, for every node 𝑥 with parent 𝑝, the key in 𝑝 is smaller than or equal to the key in 𝑥.
# The entire binary heap can be represented by a single list. The left child of a parent (at position 𝑝) is the node that is found in position 2𝑝 in the list. Similarly, the right child of the parent is at position 2𝑝+1 in the list. 

class BinHeap():
    def __init__(self):
        self.heapList = [0]  # this zero is not used, but is there so that simple integer division can be used in later methods.
        self.currentSize = 0

    def heapifyup(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                # swap
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i//2

    # insert needs heapifyup
    def insert(self, k):
        self.currentSize = self.currentSize + 1
        self.heapList.append(k)
        self.heapifyup(self.currentSize)

    def heapifydown(self, i):
        print(i)
        while i*2 <= self.currentSize: # not count 0
            minchild = self.minChild(i)
            if self.heapList[i] > self.heapList[minchild]:
                self.heapList[i], self.heapList[minchild] = self.heapList[minchild], self.heapList[i]
                i = minchild

    # return the index of the smallest child
    def minChild(self, i):
        if i*2+1 > self.currentSize:
            return i*2
        else: # both exist
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i*2+1
            else:
                return i*2

    # delmin needs heapifydown
    def delmin(self):
        minval = self.heapList[1]
        # swap the min with the last value
        self.heapList[1], self.heapList[currentSize] = self.heapList[currentSize], self.heapList[1]
        self.heapList.pop()
        self.heapifydown(1)
        self.currentSize -= 1
        return minval

    # build heap with inserting one item at a time will cost O(nlogn)
    # build heap with entire list using heapifydown - O(n)
    # Because the heap is a complete binary tree, any nodes past the halfway point will be leaves and therefore have no children. 
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.heapifydown(i)
            i -= 1

if __name__ == '__main__':
    minh = BinHeap()
    minh.buildHeap([9, 5, 6, 2, 3])
    print(minh.heapList)






