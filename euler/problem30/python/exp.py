def fun(n):
    x = 0
    while n != 0:
        x += pow(n % 10,5)
        n //= 10
    return x

acc = 0
for i in range(1000,999999):
    if fun(i) == i:
        acc += i
    
print(acc)
