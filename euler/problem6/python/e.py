MAX = 100

def gauss_sum(x):
    return x*(x+1)//2


big = gauss_sum(MAX)**2
acc = 1
for j in range(2,MAX+1):
    acc += j**2

print(big - acc)

