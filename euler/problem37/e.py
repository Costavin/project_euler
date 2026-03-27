import math

counter = 11

def isPrime(n):
    lim = int(math.sqrt(n))
    if n == 1:
        return False
    if n%2 == 0 and n//2 == 1:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, lim + 1, 2):
        if n % i == 0:
            return False
    return True

def peel(direction,element):
    e = str(element)
    return isPrime(int(e[direction:])) if direction > 0 else isPrime(int(e[:direction]))


acc = 0
test = 11
while counter != 0:
    if isPrime(test):
        #peel left, peel right
        for i in range(1,len(str(test))):
            if not peel(-i,test):
                break
            if not peel(i,test):
                break
        if peel(-i,test) and peel(i,test):
            counter -= 1
            #print(test)
            acc += test
    test += 1

print(acc)
