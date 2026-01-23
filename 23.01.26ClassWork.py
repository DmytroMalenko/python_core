
# Task1

'''
num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))


while num1 < num2:
    print(f'{num1} + 1 = {num1 + 1}')
    num1 += 1



# Task2

num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))

while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
    num1 -= 1


# Task 3


num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))

while num2 >= num1:
    if num2 % 2 == 0:
        print(num2)
    num2 -= 1

'''

# Task 4

num1 = int(input("Write first number: "))
num2 = int(input("Write second number: "))
ask = int(input("Write (1 or 2):"))

if ask == '1':
        print(num1)
        num1 += 1
elif ask == '2':
        print(num2)
        num2 = - 1
else: 
       print("Erorr")
