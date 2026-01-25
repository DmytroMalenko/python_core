#Task 1
 
'''
num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))

while num1 <= num2:
    if num2 % 5 == 0:
        print(num2 / 7)
        break
        

# Task 2

num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))

while num1 <= num2:
    print(num1)
    num1 % num1 + 1
    
while num2 >= num1:
    if num2 % 2 == 0:
        print(num2)
        num2 -= 1

while num1 <= num2:
    if num1 % 7 == 0:
        print(num1)
    num1 = num1 + 1

while num1 <= num2:
    if num2 % 5 == 0:
        print(num2 / 5)
        break


# Task 3

number = int(input("Write first number: "))
number = int(input("Write second number: "))

if number % 3 == 0:
    print(f" {number} / 3 = {number / 3}")
    print("Fizz")
else:
    print("Error")

if number % 5  == 0:
    print(f" {number} / 5 = {number / 5}")
    print("Buzz")
else:
    print("Error")

if number % 3 == 0 and number % 5 == 0:
    print(f" {number} / 3 and 5 = {number / 3 and 5}")
    print("Fizz Buzz")
else:
    print("Error")


# Task 4

num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))
step = int(input("Write step: "))

chose = input("Write (f or g) f- forward order, g - reverse order: ")


if chose == 'f':
    while num1 <= num2:
        print(num1)
        num1 += step
elif chose == 'g':
    while num1 >= num2:
        print(num1)
        num1 -= step
else:
    print("Erorr")



# Task 5

num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))

one = 1
while num1 <= num2:
    if num1 % 4 == 0 and num1 % 6 != 0:
        one *= num1
        num1 += 1
else:
    print("No numbers are divisible by 4 and  by 6.")



# Task 6

A = int(input("Write A: "))
N = int(input("Write N: "))

while A >= N:
    if N == '1':
        print(f'{A} * 1 = {A * 1}')
    print(A)
    break

if N == '2':
    print(f'{A} * {A} = {A* A}')
elif N == '3':
    print(f'{A} * {A} * {A}= {A * A * A}')
elif N == '4':
    print(f'{A} * {A} * {A} * {A}= {A * A * A * A}')
elif N >= '5':
    print(f'{A} * {A} * {A} * {A} * {A} = {A * A * A * A * A}')
else: 
    print("Erorr")

'''

