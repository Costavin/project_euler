a,b,index = 1,1,2
state = True
while state:
    index += 1
    a,b = b,a+b
    if len(str(b)) >= 1000:
        state = False

print(b,index)
