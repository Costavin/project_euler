import math

def isPrime(n):
    l = int(math.sqrt(n))
    for i in range(3,l+1,2):
        if (n % i == 0):
            return False
    return True

#append the tail to the head
def cycle(n):
    h = int(n)
    return int(str(h)[-1] + str(h)[:-1])

def genValue(lis):
    for i in lis:
        for j in lis:
            yield int("".join(map(str,(i,j))))
            for k in lis:
                yield int("".join(map(str,(i,j,k))))
                for l in lis:
                    yield int("".join(map(str,(i,j,k,l))))
                    for m in lis:
                        yield int("".join(map(str,(i,j,k,l,m))))
                        for n in lis:
                            yield int("".join(map(str,(i,j,k,l,m,n))))

limit = 1_000_000

#6 char max combination 
odd = [1,3,5,7,9]

acc = 5
for n in genValue(odd):
    if not isPrime(n):
        pass
    else:
        comp = cycle(n)
        p_acc = 1
        while (comp != n):
            if isPrime(comp):
                p_acc += 1
            if p_acc == len(str(comp)):
                acc += 1
                #print(n)       #in case we wanna see the primes
            comp = cycle(comp)
    

print(acc)
