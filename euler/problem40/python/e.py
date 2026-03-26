limit = 1_000_000

def c(index): #12
    if index//10 < 1:               #unit
        return index
    elif index//190 < 1:                            #10-100 -> 90*2+10 
        return str((index + 10)//2)[index % 2]
    #at 190 it should give 1 (of 100)
    elif index//2890 < 1:                           #1000*3-110=x
        new_v = (index+110)                     #(190+110)//3 = 100; 999*3-110 = 2887
        return str(new_v//3)[new_v % 3]
    elif index//38890 < 1:                         #2890 + 1110 // 4 = 1000 until 10000-1
        new_v = (index + 1110)
        return str(new_v//4)[new_v % 4]
    elif index//488890 < 1:
        new_v = (index + 11110)
        return str(new_v//5)[new_v % 5]
    elif index//4888890 < 1:
        new_v = (index + 111110)
        return str(new_v//6)[new_v % 6]
    else:
        new_v = (index + 1111110)
        return str(new_v//7)[new_v % 7]


#print(c(1),c(10),c(100),c(1_000),c(10_000),c(100_000),c(1_000_000))
print(int(c(1))*int(c(10))*int(c(100))*int(c(1_000))*int(c(10_000))*int(c(100_000))*int(c(1_000_000)))


