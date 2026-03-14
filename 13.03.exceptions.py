#my_list =  ['orange', 'apple', 'banana']

# print(my_list[10])
# print(10 / 0)
# def recursion():
#     recursion()

# var = recursion()

# var()

operators = ['+', '-', '*', '/']
while(True):
    try: 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        action = input("Enter operation (+,-,*,/): ")
        if action not in operators:
            raise Exception(action)
        match action:
            case '+': print(f'{num1} + {num2} = {num1 + num2}')
            case '-': print(f'{num1} - {num2} = {num1 - num2}')
            case '*': print(f'{num1} * {num2} = {num1 * num2}')
            case '/': print(f'{num1} / {num2} = {num1 / num2}')
    except ZeroDivisionError:
        print("You can't dilitu na 0!")
    except ValueError: 
        print("Uncorecct number!")
    except Exception as ex:
        print(f"Uncorrect operations! {ex.args[0]}")
    finally:
        repeat = input("Continue? Y/N ")
    if repeat.lower() == 'n':
            break 
















