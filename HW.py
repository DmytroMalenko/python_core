'''
print("To be\nor not\nto be") # task 1
print()
print("''Life is what happens\n\t when\n\t you're busy making " \
"other plans''\n\t John Lennon") # task 2
print()
print("''The best way to predict the future \n\tis" \
" to\n\t\tinvent it.''\n\t\t\t Alan Kay") #task 3

# HW from 12.12.2025
print("My autobiography.")
print("My name is Dmytro, I`m 16 years old.")
print("I live in Germany.")
print("I like play computer games.")
print()
print("Top 5 the best computer games:")
print("1. Rust.")
print("2. Fortnite.")
print("3. Hearts of Iron IV.")
print("4. Minecraft. ")
print("5. Roblox.")
print()
print("Top 5 the best films:")
print("1. Squid Game.")
print("2. Harry Potter.")
print("3. Man Vs Baby.")
print("4. Home Alone.")
print("5. Charlie and the Chocolate Factory.")
print()
print("My hobby is programming. I like it.")

# HW 19.12.2025
# Task 1

number1 = float(input("Write first number:"))
number2 = float(input("Write second number:"))
number3 = float(input("Write thord number:"))

print(type(number1))
print(type(number2))
print(type(number3))

print(f"{number1} * {number2} * {number3} = {number1 * number2 * number3}")

# Task 2

number1 = float(input("Write first number:"))
number2 = float(input("Write second number:"))

number3 = 2
float = number3

print(type(number1))
print(type(number2))
print(type(number3))

print(f"({number1} * {number2}) / {number3} = {(number1 * number2) / number3}")

# Task 3

number1 = float(input("Write a salary:"))
number2 = float(input("Write a credit payment:"))
number3 = float(input("Write an untilities debt:"))

print(type(number1))
print(type(number2))
print(type(number3))

print(f"{number1} - {number2} - {number3} = {number1 - number2 - number3}")

print("Money left:," f"{number1 - number2 - number3}")

# Task 4

number1 = float(input("Write distance in km:"))
number2 = float(input("Write fuel comsumption per 100 km:"))
number3 = float(input("Write price per liter:"))

number4 = 100
float = number4

print(type(number1))
print(type(number2))
print(type(number3))
print(type(number4))

print(f"{number1} / {number4} * {number2} = {number1 / number4 * number2}") # fuel used
print("Fuel used:")
print(f"{number1} / {number4} * {number2} * {number3} = {number1 / number4 * number2 * number3}") # Cost
print("Cost:")

# Task 5

number1 = float(input("Write a bill:"))
number2 = float(input("Write number of people:"))

tip = number1 * 0.15

print("Tips:", tip)
print(f"{number1} + {tip} = {number1 + tip}") # total with tip
print("Total with tip:")
print(f"({number1} + {tip}) / {number2} = {(number1 + tip) / number2}")
print("Per person:")

'''
# Task 6

number1 = float(input("Write rental price per day:"))
number2 = float(input("Write number of days:"))
number3 = float(input("Write deposit amount:"))

print(type(number1))
print(type(number2))
print(type(number3))

print(f"{number1} * {number2} = {number1 * number2}") # rent total
print(f"({number1} * {number2}) + {number3} = {(number1 * number2) + number3}") # total with deposit
print(f"{number1} * {number2} = {number1 * number2}") # after return
print(f"{number1} * {number2} / {number2} = {number1 * number2 / number2}") # per day 

print("Total with deposit",f"{(number1 * number2) + number3}")
print("Amount to pay after return:",f"{number1 * number2}")
print("Price per day:",f"{number1 * number2 / number2}")