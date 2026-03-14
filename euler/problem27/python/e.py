#n**2 + a*n + b
import math

def is_prime(value):
    if value%2==0:
        return False
    limit = int(math.sqrt(int(value)))
    for i in range(3,limit+1,2):
        if value%i==0:
            return False
    return True

def eq_check(n,a,b):
    return n*n + a*n + b

state = True
acc,a_max,b_max = 0,-1000,-1001
for b in range(-1000,1001):
    for a in range(-999,1000):
        n = 0
        state = True
        while state:
            eq = eq_check(n,a,b)
            if ((eq < 0) or (not is_prime(eq))):
                if n > acc:
                    a_max,b_max,acc = a,b,n
                state = False
            else:
                n += 1

print(acc,a_max,b_max,a_max*b_max)
        



