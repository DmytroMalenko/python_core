# Task 1
'''
while(True):
    try:
        num1 = float(input("Write first num: "))
        num2 = float(input("Write second num: "))


        match num1:
            case num1: 
                    print(f"{num1} / {num2} = {num1 / num2}")


    except ValueError: 
        print("Incorrect number!")
    except ZeroDivisionError:
        print("You can't divide by 0!")
    finally: 
        print("Завершення операції.")
    break
'''
    

# Task 2
'''
while(True):
    try:
        list_num = [10,20,30,40,50,60,70,80,90,100]
        
        index = int(input("Write index of element: "))

        match list_num:
            case list_num:
                print(list_num[index])

    except ValueError: 
        print("Incorrect index!")
    except IndexError:
        print("Iндекс виходить за межі списку!")
    finally: 
        print("Завершення операції.")
    break
'''
    


# Task 3
'''
while(True):
    try: 
        sales = input("Write your sales data: ")
        
        total_sales = []
        sales_split = sales.split()


        for i in sales.split():
            total_sales.append(float(i))

        match total_sales:
            case total_sales: 
                    total_sum = sum(total_sales)
                    print(total_sum)

    except ValueError: 
        print("Incorrect number!")
    finally:
        print("Завершення обробки.")
    break
    
'''


# Task 4
'''
while(True):
    try: 
        num = float(input("Write number: "))    

        match num:
            case num: 
                if num < 0:
                    print("Не можна обчислити квадратний корінь від'ємного числа")
                elif num > 0:
                    print(f'{num} * {num} = {num * num}')

    except ValueError: 
        print("Incorrect number!")
    finally:
        print("Завершення обчислень.")
    break
'''

# Task 5

'''
while(True):
    try: 
        product = input("Write data of a product(name, price, number): ")

        name, price, number = product.split(",")
        price = float(price)
        number = int(number)

        match product:
            case product:
                    print(name)
                    print(price)
                    print(number)
    except ValueError: 
        print("Incorrect date!")
    finally:
        print("Завершення парсингу.")
    break
'''

# Task 6


while(True):
    try: 
        import random

        def connect_to_server():
            y = random.randint(0,1)

            if y == 1: 
                print("Успішне підключення.")
            else: 
                raise ConnectionError("Помилка підключення.")
            
        connect_to_server()
    except ConnectionError:
        print("Не вдалося підключитися до сервера.")
    finally:
        print("Спробу завершено.")
    break















