"""

binary search - O(logn)

"""

def binarySearch(alist, item):
    found = False
    left = 0
    right = len(alist) - 1
    while left <= right and not found:
        mid = (right - left) // 2 + left
        # print(left, mid, right)
        if alist[mid] == item: # when alist is unique
            found = True
        elif alist[mid] < item:
            left = mid + 1
        else: 
            right = mid - 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

# recursive version
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item: # when alist is unique
            return True
        elif alist[mid] < item:
            return binarySearch(alist[mid+1:], item)
        else: 
            return binarySearch(alist[:mid], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))