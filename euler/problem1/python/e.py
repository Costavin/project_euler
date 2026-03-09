import time

def gauss_sum(val):
    p = limit//val
    return val*p*(p+1)//2

# Record the start time
acc = 0
limit = 999
start_time = time.perf_counter()

for i in range(1,limit+1):
    if (i%3==0) or (i%5==0):
        acc+=i
end_time = time.perf_counter()

print(str(acc) + "\nfor loop\nElapsed time: " + str(end_time - start_time))

start_time = time.perf_counter()
res = gauss_sum(3) + gauss_sum(5) - gauss_sum(15)

end_time = time.perf_counter()

print(str(res) + "\nGauss formula\nElapsed time: " + str(end_time - start_time))


