import math
target= 2000000

def isPrime(x):
    for i in range(3,int(math.sqrt(x)) +1):
        if x%i==0:
            return False
    return True

acc=2+3+5+7+11+13
for i in range(17,target,2):
    if (isPrime(i)):
        acc += i
print(acc)
