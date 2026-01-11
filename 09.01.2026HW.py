
# Task 1
'''
daynumber = float(input("Whrite number of a day: "))

if daynumber == 1:
    print("Monday")
elif  1 <= daynumber < 2:
    print("Tuesday")
elif 2 <= daynumber <3 :
    print("Wednesday")
elif 3 <= daynumber <= 4:
    print("Thursday")
elif 4 <= daynumber <= 5:
    print("Friday")
elif 5 <= daynumber <= 6:
    print("Saturday")
elif 6 <= daynumber <= 7:
    print("Sunday")
else:
    print("Error, whrite 1-7.")


# Task 2

monthnumber = float(input("Whrite number of a month: "))

if monthnumber == 1:
    print("January")
elif 1 <= monthnumber <= 2:
    print("February")
elif 2 <= monthnumber <= 3:
    print("March")  
elif 3 <= monthnumber <= 4:
    print("April")
elif 4 <= monthnumber <= 5:
    print("May")
elif 5 <= monthnumber <= 6:
    print("June")
elif 6 <= monthnumber <= 7:
    print("July")
elif 7 <= monthnumber <= 8:
    print("August")
elif 8 <= monthnumber <= 9:
    print("September")
elif 9 <= monthnumber <= 10:
    print("October")
elif 10 <= monthnumber <= 11:
    print("November")
elif 11 <= monthnumber <= 12:
    print("December")
else:
    print("Error, write 1-12!")



#Task 3

summa = float(input("Whrite, how many do you spend: "))
age = int(input("How old are you?: "))
discount1 =  10
discount2 = 5
discount3 = 15

if age <= 17:
    print(f'{summa} * {discount1} / 100  = {summa * discount1 /100}')
    print(f'{summa} - ({summa} * {discount1} / 100) = {summa - (summa * discount1 /100)}')
    print("Congratulations, you have discount 10%, because you are", age, end=" ")
    print("years.")

if 18 <= age <= 60:
    print(f'{summa} * {discount2} / 100  = {summa * discount2 /100}')
    print(f'{summa} - ({summa} * {discount2} / 100) = {summa - (summa * discount2 /100)}')
    print("Congratulations, you have discount 5%, because you are", age, end=" ")
    print("years.")

if age >= 61:
    print(f'{summa} * {discount3} / 100  = {summa * discount3 /100}')
    print(f'{summa} - ({summa} * {discount3} / 100) = {summa - (summa * discount3 /100)}')
    print("Congratulations, you have discount 15%, because you are", age, end=" ")
    print("years.")


#Task 4

lesson1 = float(input("Write, which mark do you have in math: "))
lesson2 = float(input("Write, which mark do you have in physics: "))
lesson3 = float(input("Write, which mark do you have in biology: "))

if lesson1 <= 2:
    print("Unsatisfactorily")
elif 4 <= lesson1 <= 5:
    print("Perfectly")
else:
    print("Error, write a mark 1-5.")


if lesson2 <= 2:
    print("Unsatisfactorily")
elif 4 <= lesson2 <= 5:
    print("Perfectly")
else:
    print("Error, write a mark 1-5.")


if lesson3 <= 2:
    print("Unsatisfactorily")
elif 4 <= lesson3 <= 5:
    print("Perfectly")
else:
    print("Error, write a mark 1-5.")



# Task 5

lesson1 = float(input("Write, which mark do you have in math: "))
lesson2 = float(input("Write, which mark do you have in physics: "))
lesson3 = float(input("Write, which mark do you have in biology: "))
lesson4 = float(input("Write, which mark do you have in history: "))

if lesson1 < 3 or lesson2 < 3 or lesson3 < 3 or lesson4 < 3:
    print("You cannot be admitted to the exam.")
elif 3 <= lesson1 or lesson2 or lesson3 or lesson4 <= 5:
    print("You have been admitted to the exam.")
else:
    print("In ohter cases, admisson to the exam is possible.")

'''

# Task 6

age = float(input("Write, how old are your car: "))
mileage = float(input("Write, which mileage had your car: "))

if age <= 3 and mileage <= 30000:
    print("A car is in excellent condition.")
elif 4 <= age <= 10 and mileage <= 100000:
    print("A car is in good condition.")
else:
    print("A car need to check")
