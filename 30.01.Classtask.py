# task 1
'''
num1 = int(input("Write number: "))

print(f'{num1} * 1 = {num1 * 1}')
print(f'{num1} * 2 = {num1 * 2}')
print(f'{num1} * 3 = {num1 * 3}')
print(f'{num1} * 4 = {num1 * 4}')
print(f'{num1} * 5 = {num1 * 5}')
print(f'{num1} * 6 = {num1 * 6}')
print(f'{num1} * 7 = {num1 * 7}')
print(f'{num1} * 8 = {num1 * 8}')
print(f'{num1} * 9 = {num1 * 9}')
'''
# Task 2
'''
for i in range(1,10):
    for j in range(1,10):
        print(f'{i} * {j} = {i * j}')
        print()

'''

# Task 3


# Task 4 
num1 = int(input("Write a number: "))

import random
from random import randint
random_number = random.randint(0,501)
random_number = randint(0,500)

if random_number == num1:
    print("Very good!")
elif random_number != num1:
    print(random_number < num1)
elif random_number != num1:
    print(random_number > num1)
    print(random_number)
    0 = input("Write 0 to quit: ")
if 0 == '0':
    break