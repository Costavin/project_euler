def leap_year(n):
    if n % 400 == 0:
        return True
    if (n % 4 == 0) and (n % 100 != 0):
        return True
    return False

def check_year(start_day, year):
    first_month_sundays = 0
    counter = start_day
    bool_leap = leap_year(year)
    if  counter % 7 == 0:
        first_month_sundays += 1
    for i in range(0,len(months)):
        if bool_leap and i == 1:
            counter += 1
        counter += months[i]
        if counter % 7 == 0 and i != len(months) - 1:   #prevent to start counting the next year
            first_month_sundays += 1
    return first_month_sundays, counter%7


months = [31,28,31,30,31,30,31,31,30,31,30,31]

acc, new_sun = 0, 0
first_day = 1
for i in range(1900,2001):
    new_sun, first_day = check_year(first_day,i)
    acc += new_sun

offset,_ = check_year(1,1900)

print(acc-offset)

