"""
merge sort: - O(nlogn) 

Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. 

"""

def mergeSort(alist):
    print("splitting: ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf, righthalf = alist[:mid], alist[mid:]

        # Remember mergesort doesn't work on the right half of the list until the left half is completely sorted.
        mergeSort(lefthalf) 
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

    print("Merging: ", alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
