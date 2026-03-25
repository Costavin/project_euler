import itertools

def comb(a):
    if len(a) > 1:
        return list(itertools.permutations(a,len(a)))
    return a

def product(a,b,c):
    aa = comb(a)
    bb = comb(b)
    acc = 0
    for e_ in aa:
        for e__ in bb:
            v_1 = "".join(str(x+1) for x in e_)
            if type(e__) != int:
                v_2 = "".join(str(x+1) for x in e__)
            else:
                v_2 = str(e__+1)
            v_3 = "".join(str(x+1) for x in c)

            if sorted(str(int(v_2)*int(v_1))) == sorted(str(v_3)):
                #print(v_1,v_2,v_3)
                if int(v_1)*int(v_2) not in products:
                    acc += int(v_2)*int(v_1) #need to join
                    products.append(int(v_1)*int(v_2))
    return acc

def check(a,b,c):
    if (len(a)+len(b) in (len(c),len(c)+1)):
        return True
    return False

def comp_sum(a,b,c):
    if check(a,b,c):
        return product(a,b,c)

products = []
limit = 9
indexes = [0,1,2,3,4,5,6,7,8]

acc = 0
for i in range(0,limit):
    for j in range(i+1,limit):
        for k in range(j+1,limit): 
            pool = indexes.copy()
            pool.remove(i)
            pool.remove(j)
            pool.remove(k)
            for l in pool:
                second_pool = pool.copy()
                second_pool.remove(l)
                for m in second_pool:
                    last = second_pool.copy()
                    last.remove(m)
                    acc += comp_sum([i,j,k],[l,m],last)
            for l in range(k+1,limit):
                second_pool = pool.copy()
                second_pool.remove(l)
                for m in second_pool:
                    last = second_pool.copy()
                    last.remove(m)
                    acc += comp_sum([i,j,k,l],[m],last)
print(acc)

