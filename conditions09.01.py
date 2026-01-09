

'''
#Користувач вводить число. Дізнатись чи це число входить у діапазон від 10 до 20
# Kalkulyator: + - * /
number1 = float(input("Whrite first number: "))
number2 = float(input("Whrite second number: "))
opreration = input("Whrite (+,-,*,/): ")

match operation:
    case '+':
        print(f'{number1} - {number2} = {number1 - number2}')
    case '-':
        print(f'{number1} - {number2} = {number1 - number2}')
    case '*':
        print(f'{number1} - {number2} = {number1 - number2}')
    case '/':
        if number2 == 0:
            print(" You can't / at 0!")
        else: 
            print(f'{number1} / {number2} = {number1 / number2}')
         else: 
        print("Unbecanteble symbole!")

number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
operation = input("Введіть оператор (+, -, *, /): ")

if operation == '+':
    print(f'{number1} + {number2} = {number1 + number2}')
elif operation == '-':
    print(f'{number1} - {number2} = {number1 - number2}')
elif operation == '*':
    print(f'{number1} * {number2} = {number1 * number2}')
elif operation == '/':
    if number2 == 0:
        print('Не можна ділити на нуль!')
    else:
        print(f'{number1} / {number2} = {number1 / number2}')
else:
    print("Невідомий оператор!")






#number = int(input("Whrite  a number: "))

#if number >= 10 and number <= 20:
#    print(f"{number} true number")
#else:
#    print(f"{number} False number")


print(f"True and True = {True and True}")
print(f"False and True = {False and True}")
print(f"True and False = {True and False}")
print(f"False and False = {False and False}")

print(f"True or True = {True or True}")
print(f"False or True = {False or True}")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")


print(f'not False = {not False}')
print(f'not True = {not True}')


print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(4))
print(bool(10.5))
print(bool('Hello'))

name = None
print(bool(name))


temperature  = int(input("Which temperature is out?"))

if temperature  <= 0:
    print('To wear shapky')
    print('To wear shyby')
    print('To wear termobilisny')
    print('To wear shyby')
elif  (( temperature  > 0) and (temperature < 15)):
    print('To wear kyrtky')
    print('To wear shapky')
else:
    print('To wear T-Shirt')    
    print('To wear Kepky ')

print('To go out')



# Operatoru porivnnyanya
number = int(input("Write a number: "))

print(f'{number} > 10? {number > 10}')
print(f'{number} < 10? {number < 10}')
print(f'{number} > 10? {number > 10}')
print(f'{number} >= 10? {number >= 10}')
print(f'{number} <= 10? {number <= 10}')
print(f'{number} == 10? {number == 10}')
print(f'{number} != 10? {number != 10}')

PI = 3.14

can_pinguins_swim = True
can_pinguins_fly = False

print(f'Pinguins can swim: {can_pinguins_swim}')
print(f'Pinguins can fly: {can_pinguins_fly}')
print(type(can_pinguins_swim))
print(type(can_pinguins_fly))
'''




