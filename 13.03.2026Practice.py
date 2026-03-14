# Task 1
'''
while(True):
    try:
        without_discount = float(input("Write price of the product: "))
        with_discount = float(input("Write a dscount(1-100): "))

        match with_discount:
            case with_discount: 
                finally_price = print(f"{without_discount} * {with_discount} / 100 = {without_discount * with_discount / 100}")

    except ValueError: 
        print("Incorrect number!")
    finally:
        repeat = input("Repeat? Y/N")
    if repeat.lower() == 'n':
        break
        
# Task 2
while(True):
    try: 
        dollars = float(input("Write price in dollars: "))
        print("1 dollar = 0,87Euro.")
        if dollars == 0:
            raise Exception(dollars)

        match dollars:
             case dollars:
                print(f'{dollars} * 0.87 = {dollars * 0.87}') 
    except ValueError: 
        print("Incorrect number!")
    except Exception as ex:
        print(f"Курс обміну не може дорівнювати нулю. {ex.args[0]}")
    finally: 
        repeat = input("Repeat? Y/N")
    if repeat.lower() == 'n':
        break
        

# Task 3

while(True):
    try: 
        marks = input("Write your marks(1-100): ")
        
        total_mark = []
        marks_split = marks.split()

        for i in marks.split():
            total_mark.append(float(i))

        total_sum = 0

        for mark in total_mark:
            total_sum += mark

        match total_mark:
            case total_mark: 
                    average = total_sum / len(total_mark)
                    print(average)

    except ValueError: 
        print("Incorrect number!")
    except ZeroDivisionError:
        print("Your list is empty!")
    finally:
        print("Завершення обчислень")
    break


# Task 4

bank = 5000

while(True):
    try:
        summa = input("Write sum of money to withdraw: ")

        summa = float(summa)
        if summa <= 0:
            raise Exception("Некоректна сума для зняття.")
    
        match summa:
            case summa:
                if summa > bank:
                    print("Not enough balance.")
                elif summa % 10 != 0:
                    print("Amount must be a multiple of 10")
                elif summa <= 0:
                    print("Amount must be greater than 0!")     
                elif summa % 10 == 0:
                    print("Take your money:", summa)
    except ValueError: 
        print("Incorrect number!")
    except Exception as ex:
        print("Некоректна сума для зняття.")
    finally:
        print("Завершення транзакції.")
    break



# Task 5

while(True):
    try: 
        order_num = input("Write your order number: ")
        num = order_num[3:]
        num = int(num)


        match order_num:
            case order_num: 
                if order_num[0:3] != 'ORD':
                    print("Incorrect order, without 'ORD'!")

                elif order_num[0:3] == 'ORD':
                    print("Order number is valid!")   
    except ValueError: 
        print("Incorrect number!")
    except Exception as ex:
        ("Неправильний формат номера замовлення.")
    finally:
        print("Завершення перевірки.")
    break
'''

# Task 6

while(True):
    try: 
        num = input("Write num: ")
        
        total_numbers = []
        num_split = num.split()
        total_sum = 0

        for i in num.split():
            total_numbers.append(float(i))

        for i in total_numbers:
            total_sum += i

        match total_numbers:
            case total_numbers: 
                    average = total_sum / len(total_numbers)
                    print(average, 'Average.')
                    print(total_sum, 'Sum.')

    except ValueError: 
        print("Warning: incorrect value skipped ->", i)
    except ZeroDivisionError:
        print("Your list is empty!")
    finally:
        print("Завершення обробки даних.")
    break














