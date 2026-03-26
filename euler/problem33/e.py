import math

def simplify(a,b):
    for i in range(2,int(math.sqrt(a))+1):
        while (a%i == 0) and (b%i == 0):
            a = a//i
            b = b//i
    return a,b

def compute(a,b,c):
    n_m = a*10 + c 
    n_d = b*10 + c
    if (n_m / n_d == a / b):
        return True, n_d, n_m
    n_m = c*10+a
    n_d = c*10+b
    if (n_m / n_d == a / b):
        return True, n_d, n_m
    if a < c:
        n_m = a*10+c
        n_d = c*10+b
        if (n_m / n_d == a / b):
            return True, n_d, n_m
    return False, None, None

max_den = 1
max_num = 1
for num in range(1,10):
    for den in range(num+1,10):
        for new_char in range(1,10):
            res , d_, n_ = compute(num,den,new_char)
            if res:
                print(n_,d_)
                max_num *= n_
                max_den *= d_
print(max_num,max_den,simplify(max_num,max_den))
            

