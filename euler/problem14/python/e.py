target = 1_000_000

import math

def collatz_red(n):
    if n%2 == 0:
        return n // 2
    return 3*n + 1


def countChain(n):
    if (str(n) in memory):
        return memory[str(n)]
    if n % 2 == 0:
        memory[str(n)] = 1 + countChain(n // 2)
    else:
        memory[str(n)] = 2 + countChain((3*n + 1) // 2)
    return memory[str(n)]
        
def long_version():
    l=[]
    longest=[]
    generator = 1
    for i in range(3,target):
        tgt = i
        l = [i]
        while tgt != 1:
            tgt = collatz_red(tgt)
            l.append(tgt)
        if len(l) > len(longest):
            longest = l
            generator = i
    return len(longest), generator


print(long_version())

memory = {"1":1}
longest_c = 1
val = 1
for i in range(target//2,target):
    if countChain(i) > longest_c:
        longest_c = countChain(i)
        val = i
print(longest_c,val)
