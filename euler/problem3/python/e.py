

target = 600851475143
factor = []

def reduce(value,index):
    if value%index ==0:
        while value%index == 0:
            factor.append(index)
            value /= index
    return value
    

reduce(target,2)
for i in range(3, int(target**(1/2)),2):
    if target % i == 0:
        print(i)
        target = reduce(target,i)

print(factor)

acc=1
for x in factor:
    acc*=x
print(acc)
