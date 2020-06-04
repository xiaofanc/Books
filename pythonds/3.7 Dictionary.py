"""
ditionary:
get, set, delete, contains - O(1)
iteration, copy - O(n)

"""
# contains in list - O(n)
# compare contains in list and dictionary

import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))

# 10000,      0.088,      0.002
# 30000,      0.275,      0.002
# 50000,      0.446,      0.002
# 70000,      0.629,      0.002
# 90000,      0.790,      0.002
# 110000,      0.987,      0.002 ....