#repeating cycle would require matching the same numerator again
#no need to save the chain of remainders, but the cycle of numerator

def count_num(numerator, denominator):
    count = -1
    num_vec = set()
    while ((numerator != 0) and (numerator not in num_vec)):
        num_vec.add(numerator)
        numerator %= denominator
        numerator *= 10
        count += 1
    return count

target,result,index = 1000,0,0
for i in range(2, target):
    scale = 100 if i < 100 else 100 if i < target else 10
    acc = count_num(1, i)
    if acc > result:
        result = acc
        index = i

print(result, index)
