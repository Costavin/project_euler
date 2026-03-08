target = 4000000
#target = 10

a = 1
b = 2
acc_even = 0
state = True
while (state):
    a += b
    a,b = b,a
    if (a % 2 == 0):
        acc_even += a
    if (b > target):
        state = False
print(b,a,acc_even)
