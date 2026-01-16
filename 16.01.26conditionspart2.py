'''
number = int(input("Write a number: "))

# Short tile of if
# if number % 2 == 0: print(f'Number {number} parne.')

print(f"Number {number} parne.") if number % 2 == 0 else print(f'Number {number} dont parne')

num1 = 10
num2 = 15

( print(f"num1") ) if (num1 > num2) else  ( print((f"num2")) if (num2 > num1) else (print('==')))

# 10 + 12 - binarni operarots
# -(-10)  - ynarni operator

age = 10
if age >= 10:
    pass # TODO: Add underage logic later
else:
    print("Access granted")


day = int(input('Write a number of a day: '))

match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Don't corect number of day")

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4: 
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else: 
    print("Error, not corect day")

month = int(input("Write number of month: "))

match month:
    case 12 | 1 | 2: print("Winter")
    case 3 | 4  | 5: print("Vesna")
    case 6 | 7  | 8: print("Summer")
    case 9 | 10 | 11: print("Osin")
    case _: print("Eror")

day = int(input("Write number of day: "))
match day:
    case 1 | 2 | 3 | 4 |5 if month == 1:
        print("Work day february")
    case 6 | 7  if month == 1:
        print("not work day february")
    case 1 | 2 | 3 | 4 |5 if month == 2:
        print("Work day jenuary")
    case 6 | 7  if month == 2:
        print(" not Work day juni")
'''

num1 = float(input("Write first number: "))
num2 = float(input("Write second number: "))
acction = input("Write (+, -, *, /, %, //, **):")

match acction:
    case '+': print(f'{num1} + {num2} = {num1 + num2}')
    case '-': print(f'{num1} - {num2} = {num1 - num2}')
    case '*': print(f'{num1} * {num2} = {num1 * num2}')
    case '/':
        if num2 == 0:
            print("You can't diliti at 0")
        else: 
            print(f'{num1} / {num2} = {num1 / num2}')
    case '%':
        if num2 == 0:
            print("You can't ")
        else: 
            print("You can't")
    case '//':
        if num2 == 0:
            print("You can't")
        else:
            print(f'Resalts {num1} at {num2} its {num1 // num2 }')
    case '**': print(f"{num1} at stepenni {num2} ")
    case _ :  print(f"Eror")
             


