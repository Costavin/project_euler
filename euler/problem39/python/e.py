import math

perimeter = 1000
max_ = 0
dict_pers = dict()

for a in range(1,perimeter):
    for b in range(1,perimeter):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer():
            key = a+b+int(c)
            if key <= perimeter:
                if key not in dict_pers: 
                    dict_pers[key] = 1
                else:
                    dict_pers[key] += 1


print([x for x,y in dict_pers.items() if y == max(dict_pers.values())])
