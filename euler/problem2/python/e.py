import time

target = 4000000
#target = 10

a = 1
b = 2
acc_even = 0
state = True

start_time = time.perf_counter()

while (state):
    a += b
    a,b = b,a
    if (a % 2 == 0):
        acc_even += a
    if (b > target):
        state = False

end_time = time.perf_counter()

print("Elapsed time: " + str(end_time - start_time))
print(b,a,acc_even)


a,b,c,summ = 1,1,0,0
c = a+b
start_time = time.perf_counter()

while (c<target):
    summ += c
    a = b+c
    b = a+c
    c = b+a

end_time = time.perf_counter()

print("Elapsed time: " + str(end_time - start_time))
print(summ)
