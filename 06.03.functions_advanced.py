'''
def some_func(param):
    if param == 10:
        return 'some value'
    else:
        print(param)

var = some_func(10)
some_func(var)

def enclosing_fun():
    enclosing_var = 10
    def inner():
        print(enclosing_var)
    inner()
'''

def get_discounted_prices(prices: list):
    discounted_prices = []

    for price in prices: 
        if price > 100:
            new_price = price * 0.8
            discounted_prices.append(new_price)
    return discounted_prices

original_prices = [50, 120, 80, 200, 300]
discounted_prices = list(map(lambda a: a * 0.8, filter(lambda a: a > 100,original_prices)))
print(discounted_prices)


# original_prices = [50,120, 80, 200, 300]
# result = get_discounted_prices(original_prices)
# print(result)


def recursion():
    print('recursion')
    recursion()

def func_A():
    print('A calls B')
    func_B()

def func_B():
    print("B calls A")
    func_A()

'''import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())


def factorial_loop(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursion(num - 1)

print(factorial_recursion(5))
print(factorial_loop(5))

def some_func():
    print("Hello")

func_var = some_func
print(type(func_var))
func_var()

# callback function

def some_func_with_callback(callback):
    print("function that another function")
    callback()

def print_greet():
    print("Greetings!")

some_func_with_callback(some_func)
some_func_with_callback(print_greet)

'''

# sum = lambda a, b: a + b

# print(sum(10,12))

'''

operations = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a / b if b != 0 else ZeroDivisionError(" Zero division")
}

num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))
action = input("Enter ssigh (+,-,*, /): ")

if action in operations:
    print(operations[action](num1, num2))
else:
    print("Incorrect sign!")

tax_rate = 0.2

def calc_tax_impure(amount):
    return amount * tax_rate

def calc_tax_pure(amount, tax_rate):
    return amount * tax_rate
print(calc_tax_pure(10,0.3))





my_cart = ['apple', 'banana']
def add_product_impure(cart, product):
    cart.append(product)
    return cart



def add_product_pure(cart: list, product: str) -> list:
    new_cart = cart.copy()
    new_cart.append(product)
    return new_cart

new_cart = add_product_pure(my_cart, 'orange')
print(new_cart)
print(my_cart)
# add_product_impure(my_cart, 'orange')
# print(my_cart)


def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(3))
print(triple(9))




my_list = [15, 8 , 42, 4, 16, 23]
even = []

for num in my_list: # inperativni
    if num % 2 == 0:
        even.append(num)


even_number = list(filter(lambda a: a % 2 == 0, my_list)) # deklarativni

print(even_number)
'''
def changecase(func):
    def inner():
        return func().upper()
    return inner

@changecase
def my_function():
    return 'Hello, Sally!'

@changecase
def goodby():
    return 'Goodby, Sally!'

print(my_function())
print(goodby())



