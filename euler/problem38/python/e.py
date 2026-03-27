import itertools

pandig = "123456789"

def is_pand(test):
    if sorted(test) == sorted(pandig):
        return True
    return False

def product(base):
    prods = []
    for i in range(1,8):
        for x in str(int(base)*i):
            if x in prods:
                return -1
            prods.append(x)
        if len(prods) == 9:
            res = "".join(str(ch) for ch in prods)
            if is_pand("".join(res)):
                return int(res)
    return -1

def cycle_char(c, bas):
    for offset in range(0,8):
        if c not in base:
            bas_ = bas + c
        else:
            bas_ = bas
        res = product(bas_)
        if res > max_:
            return int(res)
    return -1


max_ = 0
base = pandig[-1]

for chhh in pandig:
    for chh in pandig:
        for ch in pandig:
            if cycle_char(ch+chh+chhh, base) > max_:
                max_ = cycle_char(ch+chh+chhh, base)

print(max_)
    

