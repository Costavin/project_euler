MAX = 999
MIN = 100

def check_pal(x):
    j = 0
    if (len(x)%2==1):
        j = 1
    if x[:len(x)//2] == x[j+len(x)//2:][::-1]:
        return True
    return False



result = [0,0,0]
for i in range(MAX,MIN,-1):
    for j in range(MAX,MIN,-1):
        prod = i*j
        if check_pal(str(prod)):
            if prod > result[0]:
                result = [prod,i,j]
                print(result)

print(result)
