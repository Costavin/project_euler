target = 4000000

def fibo(n):
   a,b = 0,1
   for _ in range(n):
        yield a
        a,b = b,a+b

acc = 0

for x in fibo(target):
    if x > target:
        break
    if x%2:
        acc += x


print(acc)
    

