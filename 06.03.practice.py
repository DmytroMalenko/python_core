# Task 1
'''
def func(a,b):
    if b == 1:
        return a
    if b == 0:
        return 1
    return a * func(a, b - 1)

print(func(4,3))

# Task 2

def days_date(day1, month1, year1, day2, month2, year2):
    days1 = 0
    for i in range(1,year1):
        if (i % 400 == 0 ):
            days1 += 366
        else:
            days1 += 365

    for i in range(1,month1):
        if i in [1,3,5,7,8,10,12]:
            days1 += 31
        elif i in [2,4,6,9,11]:
            days1 += 30
        else: 
            if (year1 % 400 == 0):
                days1 += 29
    else:
        days1 += 28
        days1 += day1

        days2 = 0
    for i in range(1,year2):
        if (i % 400 == 0 ):
            days2 += 366
        else:
            days2 += 365

    for i in range(1,month2):
        if i in [1,3,5,7,8,10,12]:
            days2 += 31
        elif i in [2,4,6,9,11]:
            days2 += 30
        else: 
            if (year2 % 400 == 0):
                days2 += 29
    else:
        days2 += 28
        days2 += day2
        return abs(days1 - days2)

print(days_date(5, 4, 2020, 1, 10, 2026))
print(days_date(10, 3, 2024, 15, 3, 2025))
'''

# Task 3

num = []

for i in range(100):
    num.append(range(100))
    
def find_num(number):
    if i > len(number) - 10:
        return 0
    
    summa = 0

    for i in range(i,i + 10):
        summa += number[i]

    if summa < number:
        number = i

        return find_num(number)

position = find_num(num)

print(find_num(10))









