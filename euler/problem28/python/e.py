#+21 22 23 24 +25 26
#20  +7  8  +9 10 27
#19  6  +1   2 11 28
#18  +5  4  +3 12 29
#+17 16 15 14 +13 30
#                 31
#1,3,5,7,9, 13,17,21,25, 
#+2,+4
acc = 1
limit = 1001
step = 2
head = 1
counter = 1
while counter < limit:
    for i in range(0,4):
        head += step
        acc += head
    step += 2
    counter += 2
print(acc)
