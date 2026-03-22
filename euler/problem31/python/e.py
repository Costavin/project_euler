#1: 1
#2: 1+1, 2
#3: 1+1+1, 1+2
#4: 1+1+1+1, 1+1+2, 2+2
#5: 1+1+1+1+1, 1+2+2, 1+1+1+2, 5    #distinct, without repetitions
#6: 1+1...   , 1+1+2+2, 2+2+2, 1+1+1+1+2, 5+1
#7: 1+1...   , 1+1+1+2+2, 2+2+2+1, 1+1+1+1+1+2, 5+2, 5+1+1

coins = [1,2,5,10,20,50,100,200]
       
def dyn_prog(coins,am):
    dp = [0]*(am+1)
    dp[0] = 1
    for c in coins:
        for i in range(c, am + 1):  #include am
            dp[i] += dp[i-c]
                   #print(dp)
    return dp[am]            

target=200
print(target, dyn_prog(coins,target))


