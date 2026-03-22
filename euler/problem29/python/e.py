# 2**2, 2**3, 2**4, 2**5
#...
# 4**2, 4**3, 4**4, 4**5
# ...
#
#2 <= a <= 5, 2 <= b <= 5, count_distinnct(a**b)
#don't want to crete 'em all. it can be easily noticable that 2**4 = 4**2 (as it will be 2**6 and 4**3 (=64), 2**8 and 4**4 (=256))

e = set()
for a in range(2,101):
    for b in range(2,101):
        e.add(pow(a,b))
print(len(e))
