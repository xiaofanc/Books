"""
Selection sort: - O(n^2) 直接找出当前位置之前的最大值，然后交换，填充当前位置

The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. 

Due to the reduction in the number of exchanges, the selection sort typically executes faster then bubble sort.

"""
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        maxposition = 0
        # find the max value
        for i in range(1, fillslot+1):
            if alist[i] > alist[maxposition]:
                maxposition = i
        alist[maxposition], alist[fillslot] = alist[fillslot], alist[maxposition]

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

