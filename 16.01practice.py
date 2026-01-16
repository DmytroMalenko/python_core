
# Task 1
'''
mark = int(input("Write how many points do you have: "))

if 90 <= mark <= 100:
    print("Very good!")
elif 70 <= mark <= 89:
    print("Good")
elif 50 <= mark <= 69:
    print("Okey")
elif mark <= 50:
    print("Bad")
else:
    print("Erorr, write points 0-100.")


# Task 2 

money = float(input("How many money you get:  "))
years = float(input("How long are you work: "))

if years < 1:
    print("You don't have prize")
elif 1 <= years <= 3:
    print("You have 5% prize of money.")
elif 3 <= years <= 5:
    print("You have 10% prize.")
elif years >= 5: 
    print("Prize 15%.")
else: 
    ("Error, write correct years.")



# Task 3

number = int(input("Write a number with 4 tails: "))

if number % 2 == 0: print(f'even Number.')
else:
    print("Odd number.")


# Task 4

number = int(input("Write six-digit number: "))

num1 = number // 100000 + number // 10000 % 10 + number // 1000 % 10
num2 = number // 100 % 10 + number // 10 % 10 + number % 10

if num1 == num2:
    print("Число щасливе")
else:
    print("Число нещасливе")

'''

# Task 5

num = int(input("Write six-digit number: "))



