"""
Quick sort: - O(nlogn) 比pivot小的都在左边， 比pivot大的都在右边 worst case - O(n^2)
The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional storage.

pick up the pivot value. We will simply use the first item in the list.
According the to pivot value, find the split point and at the same time move other items to the appropriate side of the list, either less than or greater than the pivot value.

We begin by incrementing leftmark until we locate a value that is greater than the pivot value. We then decrement rightmark until we find a value that is less than the pivot value. 

[54,   26,93,17,77,31,44,55,20]
pivot  L                    R
# when R < pivot, stop
[54,   26,93,17,77,31,44,55,20]
pivot      L                 R
# exchange L and R
[54,   26,20,17,77,31,44,55,93]
pivot        L           R
[54,   26,20,17,77,31,44,55,93]
pivot            L    R
# when L > pivot stop, R < pivot stop
exchange L and R
[54,   26,20,17,44,31,77,55,93]
pivot            L    R
[54,   26,20,17,44,31,77,55,93]
pivot              L/R
[54,   26,20,17,44,31,77,55,93]
pivot              R  L
# when rightmark < leftmark, split point found, then exchange the pivot and the split point. 
[31,   26,20,17,44,54,77,55,93]
pivot              R  L 

In addition, all the items to the left of the split point are less than the pivot value, and all the items to the right of the split point are greater than the pivot value.

reselect the pivot value, then repeat the process.

RECURSION:
lefthalf
[31, 26, 20, 17, 44]  pivot = 31
      L          R
[31, 26, 20, 17, 44]  pivot = 31
              R  L  
[17, 26, 20, 31, 44] 

[17, 26, 20]  pivot = 17
      L  R 
[17, 26, 20]  pivot = 17
 R    L   

righthalf of 17
[26, 20]  pivot = 26
     L/R
[20, 26]  pivot = 26

righthalf of 31:
[44]

righthalf of 54:
[77, 55, 93] pivot = 77
     L   R
[77, 55, 93] pivot = 77
     R   L
[55, 77, 93]

[17, 20, 26, 31, 44, 54, 55, 77, 93]
       
"""

# quickSortHelper begins with the same base case as the merge sort. If the length of the list is less than or equal to one, it is already sorted. If it is greater, then it can be partitioned and recursively sorted. 
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        # splitpoint has the value of pivot in the end
        splitpoint = partition(alist, first, last)

        # everything in the left of the splitpoint(pivot) is smaller than pivot, and everything in the right is larger than pivot
        # quicksort left part
        quickSortHelper(alist, first, splitpoint-1)
        # quicksort right part
        quickSortHelper(alist, splitpoint+1, last)

# partition return splitpoint
# The partition function implements the process described earlier.
def partition(alist, first, last):
    pivot = alist[first]
    left = first + 1
    right = last
    done = False
    # compare with pivot to split the list
    while not done:
        print("wait to check: ", left, right, alist)
        while left <= right and alist[left] <= pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        # exchange left and right
        if left > right:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]
            print("after switch:  ", left, right, alist)
    # right > left, end 
    alist[right], alist[first] = alist[first], alist[right]
    print("end:           ", left, right, alist)

    return right

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

"""
[14,17,13,15,19,10,3,16,9,12] 
First partition:
[14,12,13,9,19,10,3,16,15,17] 
           L           R
[14,12,13,9,3,10,19,16,15,17] 
             L    R
[14,12,13,9,3,10,19,16,15,17] 
               R  L
[10,12,13,9,3,14,19,16,15,17] 
               R  L
second partition:
left:
[10,12,13,9,3]
     L      R
[10,3,13,9,12]
       L R
[10,3,9,13,12]
       L R
[10,3,9,13,12]
      R L 
[9,3,10,13,12]
      R L 

"""





