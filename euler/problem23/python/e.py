import math

def factorization(n):
    facts = [1]
    limit = int(math.sqrt(n))
    original = n
    if n%2==0:
        while n%2==0:
            n //= 2
            facts.append(2)
    for i in range(3,limit+1,2):
        while n%i == 0:
            n //= i
            facts.append(i)
    if n != 1 and n != original:    #lime the prime numbers
        facts.append(n)
    return facts

def comb_prop_div(factors,v): #1,2,2,2,2337
    res = set(factors)  #1,2,2337
    for i in range(0,len(factors)-1):   #we dont want 2337**2
        z = set()
        for j in res:
            if ((factors[i]*j != v) and (v % (factors[i]*j) == 0)):
                z.add(factors[i]*j)
        res.update(z)
    return res

def acc_factors(lista,value):
    return sum(lista), 1 if value < sum(lista) else 0 #if sum(lista) == value else -1

abundant= set()
sum_abundants = set()

target = 28123
sum_not_abundant = 3 #1+2
for i in range(3,target+1):
    fact = factorization(i)
    acc, ab = acc_factors(comb_prop_div(fact,i),i) #sum,state
    if ab:
        abundant.add(i)
        a = set(x+i for x in abundant)
        sum_abundants.update(a)
    if i in sum_abundants:
        pass
    else:
        sum_not_abundant += i

print(sum_not_abundant)


