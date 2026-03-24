def is_pal(val):
    #len/2 checks, 6->3 checks, 7 -> 3 checks, central char we don't care
    #is it faster than reversing the whole string and checking?
    limit = len(val)
    if limit == 1:
        return True
    for i in range(0,limit//2):
        if val[i] != val[-(i+1)]:
            return False
    return True

limit = 1_000_000

#instead of checking all the numbers, we can find a function that generates one of the two palindromes and check for the other type
acc=1
for i in range(3,limit,2):
    binary = str(bin(i)[2:])
    if is_pal(binary) and is_pal(str(i)):
        acc += i

print(acc)
