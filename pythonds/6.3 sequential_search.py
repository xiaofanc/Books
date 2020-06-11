"""

sequential search - O(n)

"""

def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found

def orderedsequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item: # early stop
            return found
        else:
            pos += 1

    return found

