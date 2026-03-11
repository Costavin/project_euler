import time
from functools import reduce

def factorial(v):
    res = 1
    for i in range(1,v):
        res*=i
    return res

def acc(value):
    return sum(map(int,list(str(value))))

s_t = time.perf_counter()
r = acc(factorial(100))
e_t = time.perf_counter()
print(f"res: {r} elapsed time {e_t - s_t}")

s_t = time.perf_counter()
r = reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])
e_t = time.perf_counter()


print(f"res: {r} elapsed time {e_t - s_t}")

