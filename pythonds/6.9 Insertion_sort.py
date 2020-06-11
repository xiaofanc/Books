"""
Insertion sort: - O(n^2) 与之前的数相比，在之前的排好序的list中找出合适位置，然后插入

It always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.

The current item is checked against those in the already sorted sublist. As we look back into the already sorted sublist, we shift those items that are greater to the right. When we reach a smaller item or the end of the sublist, the current item can be inserted.

n-1 passes

for each pass:
    first: 1 comparison
    second: 2 comparison
    ...

"""

def insertionSort(alist):
    for passnum in range(1, len(alist)):
        currentvalue = alist[passnum]
        position = passnum
        while position > 0 and alist[position-1] > currentvalue:
            # shift to the right
            alist[position] = alist[position-1]
            position = position-1
            print(passnum, alist)

        # alist[position-1] <= currentvalue
        alist[position] = currentvalue
        print(passnum, alist)


alist = [54,26,93,17,77,31,44,55,20]
print(alist)
insertionSort(alist)
print(alist)

