# create a list
# The concatenation operator is 𝑂(𝑘) where 𝑘 is the size of the list that is being concatenated. 
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

# The append method is 𝑂(1). 
def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

if __name__ == '__main__':
    import timeit
    # timeit
    # create a Timer object whose parameters are two Python statements. The first parameter is a Python statement that you want to time; the second parameter is a statement that will run once to set up the test. 
    # The timeit module will then time how long it takes to execute the statement some number of times.
    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print("concat ", t1.timeit(number=1000), "milliseconds")

    t2 = timeit.Timer("test2()", "from __main__ import test2")
    print("append ", t2.timeit(number=1000), "milliseconds")

    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print("comprehension ", t3.timeit(number=1000), "milliseconds")

    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print("list range ", t4.timeit(number=1000), "milliseconds")


# concat  1.4893415269999999 milliseconds
# append  0.11701050099999999 milliseconds
# comprehension  0.0504242909999999 milliseconds
# list range  0.021829761000000003 milliseconds


