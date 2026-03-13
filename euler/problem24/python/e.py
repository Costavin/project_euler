limit = 1_000_000-1             #as 0123456789 is already a configuration

#2 = 2!
#        01     10
#6 = 3!
#        012    021     102     120     201     210
#24 = 4!
#        1234   1243    1324    1342    1423    1432
#        2134   2143    2314    2341    2413    2431
#        3124   3142    3214    3241    3412    3421
#        4123   4132    4213    4231    4312    4321

#16 -> 12+2+2

def swap(lis,a,b):
    lis[a],lis[b] = lis[b],lis[a]
    return lis

l = ["0","1","2","3","4","5","6","7","8","9"]

def fact(v):
    res = 1
    for i in range(1,v+1):
        res *= i
    return res

def order(lista, index, new_head):
    if new_head == 0:                                           #remains unchanged
        return lista
    else:
        app,lista[index] = lista[index],lista[index+new_head]   #update the head of the list
        for i in range(index, index + new_head):
            lista[i+1],app = app,lista[i+1]
            #print(lista)
    return lista


fixed_perm = len(l)
for i in range(0, fixed_perm-1):
    left_fix = fact(fixed_perm-i-1)
    l = order(l, i, limit // left_fix)
    limit %= left_fix

print(("").join(l))
