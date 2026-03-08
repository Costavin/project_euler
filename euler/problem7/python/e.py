target = 10001

counter = 4
def isPrime(x):
    for i in range(2,x//2):
        if x%i==0:
            return 0
    return 1

i = 7
while (counter < target):
    i+=1
    if (isPrime(i) == 1):
        counter+=1

print(i)
