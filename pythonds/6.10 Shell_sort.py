"""
shell sort: - O(n^2) multiple selection sort

The shell sort, sometimes called the “diminishing increment sort,” improves on the insertion sort by breaking the original list into a number of smaller sublists, each of which is sorted using an insertion sort. The unique way that these sublists are chosen is the key to the shell sort. Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment i, sometimes called the gap, to create a sublist by choosing all items that are i items apart.

sort the sublists first, and then a final insertion sort

从index 0-3 每4个进行 insertion sort
# start:  0 gap:  4
# position:  4 currentvalue:  77
# 54 < 77, do not shift
# alist [54, 26, 93, 17, |77|, 31, 44, 55, 20]

# position:  8 currentvalue:  20
# 77 > 20, shift right
# 54 > 20, shift right
# insert 20
# alist [54, 26, 93, 17, 77, 31, 44, 55, 77]
# alist [54, 26, 93, 17, 54, 31, 44, 55, 77]
# alist [20, 26, 93, 17, 54, 31, 44, 55, 77]
...
# start:  3 gap:  4
# position:  7 currentvalue:  55
# alist [20, 26, 44, 17, 54, 31, 93, 55, 77]

"""

def shellSort(alist):
    sublistcount = len(alist) // 2
    # start:  0 gap:  4
    # start:  1 gap:  4
    # start:  2 gap:  4
    # start:  3 gap:  4
    # start:  0 gap:  2
    # start:  1 gap:  2
    # start:  0 gap:  1  - normal insertion sort

    while sublistcount > 0:
        for startposition in range(sublistcount):
            print("start: ", startposition, "gap: ", sublistcount)
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is", alist)

        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i
        print("position: ", i, "currentvalue: ", currentvalue)
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
            print("alist", alist)

        # alist[position-gap]<=currentvalue, unchanged
        alist[position]=currentvalue
        print("alist", alist)

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)


