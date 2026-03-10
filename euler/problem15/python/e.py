def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def binomial(x,y):
    if (y > x):
        x,y = y,x
    if x > y:
        other = x - y
    else:   #x==y
        other = x
    den = fact(x) * fact(other)
    num = fact(x+y)
    return num//den

print(binomial(20,20))
