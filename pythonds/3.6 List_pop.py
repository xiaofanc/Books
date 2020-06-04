# popzero O(n) and popend O(1)
import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend  = timeit.Timer("x.pop()", "from __main__ import x")

x = list(range(200000))
print(popzero.timeit(number=1000))
# 0.109610552

x = list(range(200000))
print(popend.timeit(number=1000))
# 9.060499999999361e-05

# compare the performance
for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz, pt))

