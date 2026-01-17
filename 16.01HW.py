# Task 1
'''
number = float(input("Write number: "))
power = float(input("Write power (0,1,2,3,4,5,6,7,): "))

if power == 1:
    print(f"{number}")
elif power == 2: 
    print(f"{number} * {number} = {number * number}")
elif power == 3: 
    print(f"{number} * {number} * {number} = {number * number * number}")
elif power == 4: 
    print(f"{number} * {number} * {number} * {number}= {number * number * number * number}")
elif power == 5: 
    print(f"{number} * {number} * {number} * {number} * {number} = {number * number * number * number * number}")
elif power == 6: 
    print(f"{number} * {number} * {number} * {number} * {number} * {number}= {number * number * number * number * number * number}")
elif power == 7: 
    print(f"{number} * {number} * {number} * {number} * {number} * {number} * {number}= {number * number * number * number * number * number * number}")
elif power == 0:
    print(f" {number} / {number} = {number / number}")
else: 
    print("Erorr, write power 1-7!")



Task 2

number = int(input("Write number (1-100): "))

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
if number >= 100:
    print("Error, write number 1-100!")

'''

# Task 3

print("Starters - salat and soup.")
print("Main - kitchen and fish.")
print("Desserts - ice cream and fruits")
starters = float(input("If you want starters wirte 1: "))
main = float(input("If you want main wirte 1: "))
desserts = float(input("If you want desserts wirte 1: "))
person1 = str(input("Write (person) if you buy our food every day: "))

mainsumma =  41
discount1 = 10
discount2 = 25
discount3 = 30

salat = 5
soup = 7
kitchen = 10
fish = 12
icecream = 3
fruits = 4
desserts4 = 2
person = 1000

if starters and main and desserts == 1:
    print(f"(5 + 7 + 10 + 12 + 3 + 4) * 0.9 = {(5 + 7 + 10 + 12 + 3 + 4) * 0.9} dollars")
    print("You have 10 % discount!")
else:
    print("Error")

if mainsumma >= 20:
    print(f"(5 + 7 + 10 + 12 + 3 + 4) * (1 - {discount2} / 100) = {(5 + 7 + 10 + 12 + 3 + 4) * (1 - discount2 / 100)} dollars")
    print("You have 20 % discount because your prize more 20$!")
else:
    print("Error")

if person:
    print(f"(5 + 7 + 10 + 12 + 3 + 4) * (1 - {discount3} / 100) = {(5 + 7 + 10 + 12 + 3 + 4) * (1 - discount3 / 100)} dollars")
    print("You have bonus 5 % discount because you are buy our food every day!")

answer = str(input("Do you want Soup and fish? ")) 
if answer == 'yes':
    print("You have discount 2$ for desserts!")
    print(f"{soup} + {fish}  = {soup + fruits } ")
else:
    print("Error")

if desserts4:
    print(f"(3 + 4) - {desserts4}  = {(3 + 4) - desserts4} dollars")

