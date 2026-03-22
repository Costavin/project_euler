#up_bound = 9**5
po = 5
def fun(a,b,c,d,power=po):
    return pow(a,power) + pow(b,power) + pow(c,power) + pow(d,power) 

def fun_2(a,b,c,d,e,power=po):
    return pow(a,power) + pow(b,power) + pow(c,power) + pow(d,power) + pow(e,power)

def fun_3(a,b,c,d,e,f,power=po):
    return pow(a,power) + pow(b,power) + pow(c,power) + pow(d,power) + pow(e,power) + pow(f,power)

acc = 0
vals = set()
for i in range(0,10):
    for j in range(0,10):
        for k in range(j,10):
            for l in range(i,10):
                if sorted(list(str(fun(i,j,k,l))),key=int) == sorted(list(str(i)+str(j)+str(k)+str(l)),key=int):
                                acc +=1
                                vals.add(fun(i,j,k,l))
#print(acc)
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(j,10):
                for m in range(i,10):
                    if sorted(list(str(fun_2(i,j,k,l,m))),key=int) == sorted(list(str(i)+str(j)+str(k)+str(l) +str(m)),key=int):
                                acc +=1
                                vals.add(fun_2(i,j,k,l,m))

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(k,10):
                for m in range(j,10):
                    for n in range(i,10):
                        if sorted(list(str(fun_3(i,j,k,l,m,n))),key=int) == sorted(list(str(i)+str(j)+str(k)+str(l) +str(m) + str(n)),key=int):
                                acc +=1
                                vals.add(fun_3(i,j,k,l,m,n))


print(vals)
print(sum(vals))
