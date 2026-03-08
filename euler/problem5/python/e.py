target = 20

def gcd(a,b):
    if b > a:
        a,b = b,a
    while (b > 0):
        a,b = b,a%b
    return a

res=1
for i in range(2,target):
    val = gcd(i,res)
    if val == 1:
        res *= i
    elif i - val == 0:
        continue
    else:
        res *= val

print(res)
