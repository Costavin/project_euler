#2**8 = 2**(1000) = (((1*2**1)**2)**2)**2

from functools import reduce
import time

def opt_exp(power,base):
    res = 1
    for bit in bin(power)[2:]:
        res = res**2
        if bit == '1':
            res *= base
    return res

def acc(n):
    res = 0
    for q in str(n):
        res += int(q)
    return res

result = opt_exp(1000,2)

start_time = time.perf_counter() # Record the start time
print(acc(result))
end_time = time.perf_counter() # Record the start time
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

start_time = time.perf_counter() # Record the start time
print(reduce(lambda x,y: x+y, [int(x) for x in str(result)]))
end_time = time.perf_counter() # Record the start time
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")

start_time = time.perf_counter() # Record the start time
#print(list(str(result)))
print(sum(map( int , (list(str(result))))))
end_time = time.perf_counter() # Record the start time
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")
