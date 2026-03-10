#1  1
#3  3
#6  1*2*3     2**2 = 4        1,2,3,6
#10 2*5
#15 3*5
#21 3*7
#28 1*2*2*7       (2+1)(2)    -> 1,2,4,7,14,28
#36 1*2*2*3*3    (2+1)(2+1)   -> 1,2,3,4,6,9,12,18,36
#45 3*3*5
#55 5*11
#120 [1, 2, 2, 2, 3, 5]  (3+1)(2)(2)   -> 1,2,3,4,5,6,8,10,12,15,20,24,30,40,48,60
#    
#500+ parameters =~ 2**k - (k-1)!

import math
target = 500

def fact(x):
    lis = [1]
    for i in range(2,int(math.sqrt(x))+1):
        while (x%i == 0):
            lis.append(i)
            x = x // i
    if x > 1:
        lis.append(x)
    return lis

def number_fact(lis):
    res = 1
    acc = []
    s = set(lis)
    for el in s:
        acc.append(lis.count(el) + 1)
    for i in range(1,len(acc)):
        res *= acc[i]
    return res


def triangle_gen(value):
    return value*(value+1)//2

def check_triangle(value):
    base = int(math.sqrt(value*2))
    if base*(base+1)//2 == value:
        return True
    return False

def small_div(par_max):
    N,i = 1,1
    check = True
    limit  = int(math.sqrt(par_max))
    for p in range(2,par_max+1):
        if isPrime(p):
            if p <= limit:
                a = int(math.log(par_max)/math.log(p))
            else:
                a = 1
            N *= p**a
        else:
            continue
    return N

fac = [1]
i = 1

while number_fact(fac) < 500:
    tg = triangle_gen(i)
    fac = fact(tg)
    print(i, tg, len(fac), fac)
    i+=1
