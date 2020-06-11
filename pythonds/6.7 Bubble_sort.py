"""
Bubble sort: - O(n^2) 两两相比直到最大的放后面，在所有剩下的数中继续比，找出最大值放后面

for the first pass, we will move the largest number to the end of the list
for the second pass, we will move the second largest number to the end of the list
total pass: n-1

for pass: 
    first: n - 1 comparison, move the largest value to the end
    second: n - 2 comparison, no need to compare with the last
    ...

If there is no exchange in the pass: early stop

"""
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
            print(alist)

#alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#print(alist)
#bubbleSort(alist)
#print(alist)

# if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can be modified to stop early if it finds that the list has become sorted. 
def bubbleSort(alist):
    exchange = True
    passnum  = len(alist)-1
    while passnum > 0 and exchange:  # check each pass if there is any exchange
        exchange = False
        print("passnum: ", passnum)
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
            print("i:", i, "alist: ", alist, "exchange: ", exchange)
        passnum -= 1

alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
print(alist)
bubbleSort(alist)
