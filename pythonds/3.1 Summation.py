import time

def sumOfN(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i
    #return theSum

    end = time.time()

    return theSum, end-start

#print(sumOfN(10))
for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN(10000))

def foo(tom):
    fred = 0
    for bill in range(1, tom+1):
        barney = bill
        fred += barney
    return fred

print(foo(10))

# faster
def sumOfN3(n):
   return (n*(n+1))/2

print(sumOfN3(10))
