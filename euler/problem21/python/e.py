import math

limit = 10000

def fact(n):
    limit = int(math.sqrt(n))
    facts = [1]
    original = n
    if n%2==0:
        while n%2==0:
            n //= 2
            facts.append(2) 
    for i in range(3,limit+1,2):
        while n%i == 0:
            n //= i
            facts.append(i)
    if n != 1 and n != original:
        facts.append(n)
    return facts

def check_amicable(a,b):
    if (memory[str(b)] == a) and (memory[str(a)] == b):
        return True
    return False

def sum_prop_div(factors,v): #1,2,2,2,2337
    res = set(factors)  #1,2,2337
    for i in range(0,len(factors)-1):   #we dont want 2337**2
        z = set()
        for j in res:
            if ((factors[i]*j != v) and (v % (factors[i]*j) == 0)):
                z.add(factors[i]*j)
        res.update(z)
    return res

def load_mem(i):
    factors = fact(i)
    facts_expl = sum_prop_div(factors,i)
    total = sum(facts_expl)
    memory[str(i)] = total

memory = {'1':1}
def search_sum(limit):
    acc = 0
    for i in range(2,limit):
        #in order not to count it twice
        if str(i) in memory and str(memory[str(i)]) in memory:             
            continue
        if str(i) not in memory:
            load_mem(i)
        if str(memory[str(i)]) not in memory:
            load_mem(memory[str(i)])
        bool_amic = check_amicable(i,memory[str(i)])
        if bool_amic and i != int(memory[str(i)]):
            acc += i + memory[str(i)]
    return acc

print(search_sum(limit))
