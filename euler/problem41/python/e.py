import math,itertools

#from vec, generate all the permutations, check if prime. If list finishes, peel from the last char, and check again


def isPrime(n):
    l = int(math.sqrt(n))
    for i in range(2,l+1,1):
        if (n % i == 0):
            return False
    return True

def get_perm(st):
    return list(itertools.permutations(list(st)))[::-1]

vec = "123456789"

ex = False
for i in range(0,len(vec)):
    if i == 0:
        lis_perm = get_perm(vec[:])
    else:
        lis_perm = get_perm(vec[:-i])
    for perm in lis_perm:
        if isPrime(int("".join(perm))):
            print("".join(perm))
            ex = True
            break
    if ex:
        break

