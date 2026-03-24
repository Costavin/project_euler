from functools import reduce

def fact(x):
    res = 1
    for i in range(1,x+1):
        res*=i
    return res
#reduce(lamba x,y:x*y, [y for y in range(1,x+1)],1)

def get_indexes(n):
    return [int(x) for x in list(str(n))]

lookup = dict()
lookup[0] = 1
for i in range(1,10):
    lookup[i] = fact(i)

#we need to identify the limit case
#9! = 362880; 3! = 6; 145! = 4! + 5! = 24 + 120 + 1; 9! is enough

acc = 0
for i in range(6,lookup[9]):
    temp = sum([lookup[j] for j in get_indexes(i) ])
    if i == temp:
        acc += i

print(acc)
