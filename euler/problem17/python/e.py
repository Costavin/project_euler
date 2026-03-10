v=[
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen",
"twenty",
"twentyone",
"twentytwo",
"twentythree",
"twentyfour",
"twentyfive",
"twentysix",
"twentyseven",
"twentyeight",
"twentynine",
"thirty",
"thirtyone",
"thirtytwo",
"thirtythree",
"thirtyfour",
"thirtyfive",
"thirtysix",
"thirtyseven",
"thirtyeight",
"thirtynine",
"forty",
"fortyone",
"fortytwo",
"fortythree",
"fortyfour",
"fortyfive",
"fortysix",
"fortyseven",
"fortyeight",
"fortynine",
"fifty",
"fiftyone",
"fiftytwo",
"fiftythree",
"fiftyfour",
"fiftyfive",
"fiftysix",
"fiftyseven",
"fiftyeight",
"fiftynine",
"sixty",
"sixtyone",
"sixtytwo",
"sixtythree",
"sixtyfour",
"sixtyfive",
"sixtysix",
"sixtyseven",
"sixtyeight",
"sixtynine",
"seventy",
"seventyone",
"seventytwo",
"seventythree",
"seventyfour",
"seventyfive",
"seventysix",
"seventyseven",
"seventyeight",
"seventynine",
"eighty",
"eightyone",
"eightytwo",
"eightythree",
"eightyfour",
"eightyfive",
"eightysix",
"eightyseven",
"eightyeight",
"eightynine",
"ninety",
"ninetyone",
"ninetytwo",
"ninetythree",
"ninetyfour",
"ninetyfive",
"ninetysix",
"ninetyseven",
"ninetyeight",
"ninetynine"
]
an = ["and"]
hund =[
"hundred"
]
#print(v)

#sum from 1 up to 99
units = [v[i] for i in range(0,9)]
#decs = [v[i] for i in range(9,len(v),10)]
print(units)
acc_un = sum(map(len, units))
print(acc_un)

acc = sum(map(len, v))
print(acc)

total = acc * 10 +                              \
        100*9*len(hund[0]) + (900-9)*len(an[0])   +       \
        acc_un*100 +            \
        len("thousand") + len("one")

print(total)
