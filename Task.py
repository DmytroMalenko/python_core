# Task1
'''
Even_number = True 
Odd_number = False
number = int(input("Write a number: "))


if Even_number == (f'2,4,6,8,10'):
    print("Even number")
else:
    print("Odd number")


#Task 2
Number_is_multiple7 = True
Number_is_not_multiple7 = False
number1 = int(input("Write a number: "))
number2 = 7

if Number_is_multiple7 == float:  
    print("Number is multiple 7")
else:
    print("Number is not multiple 7")
    print(f'{number1} / {number2} = {number1 / number2}')

    
# Task 3

number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))

if number1 > number2:
    print("Найбільше число:", number1)
elif number2 > number1:
    print("Найбільше число:", number2)
else:
    print("Числа рівні")


#Task 5 
number1 = float(input("Введіть суму в доларах: "))
number3 = 43.14
print("1 dollar = 43,14 Grivnya")
if number3 == 43.14:
    print(f'{number1} * {number3} = {number1 * number3}')


#Task 6
Seconds_in_day = 24 * 60 * 60
number1 = float(input("Введіть час у секундах що минув від початку дня: "))

remaining_seconds = Seconds_in_day - number1
hours = remaining_seconds
minutes = remaining_seconds % 3600
seconds = remaining_seconds % 60

print("До опівночі залишилося:")
print(f"{hours} годин, {minutes} хвилин, {seconds} секунд")

# Task 7
diameter = float(input("Введіть діаметр кола: "))
action = input("Що обчислити (площа / периметр): ")
PI = 3.14
radius = diameter / 2

if action == "площа":
    result = PI * radius ** 2
    print(f"Площа кола = {result:.2f}")
elif action == "периметр":
    result = 2 * PI * radius
    print(f"Периметр кола = {result:.2f}")
else:
    print("Помилка: введіть 'площа' або 'периметр'")


# Task 8

file_in_gb = float(input("Введіть розмір файлу (в ГБ): "))
speed_of_internet =  float(input("Введіть швидкість інтернету (біт/с): "))
file_in_bits = file_in_gb * 1024 * 1024 * 1024 * 8
time_seconds = file_in_bits / speed_of_internet

print("У чому показати час завантаження?")
print("1 - у секундах")
print("2 - у хвилинах")
print("3 - у годинах")
choice = input("Ваш вибір: ")

if choice == "1":
    print(f"Час завантаження: {time_seconds:.2f} секунд")
elif choice == "2":
    print(f"Час завантаження: {time_seconds / 60:.2f} хвилин")
elif choice == "3":
    print(f"Час завантаження: {time_seconds / 3600:.2f} годин")
else:
    print("Невірний вибір")


# Task 9

hour = int(input("Введіть кількість годин: "))

if 0 <= hour < 6:
    print("Good Night")
elif 6 <= hour < 13:
    print("Good Morning")
elif 13 <= hour < 17:
    print("Good Day")
elif 17 <= hour < 24:
    print("Good Evening")
else:
    print("Некоректне значення часу")

'''

# Task 10

temperature = float(input("Введіть температуру у °C: "))

if temperature < -10:
    print("Дуже холодно")
elif -10 <= temperature < 0:
    print("Холодно")
elif 0 <= temperature < 15:
    print("Прохолодно")
elif 15 <= temperature <= 25:
    print("Тепло")
else:
    print("Спекотно")




