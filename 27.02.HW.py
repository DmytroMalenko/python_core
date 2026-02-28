# Task 1
'''
def print_function():
    print("\"Don't compare yourself with anyone in this world...\n\tif you do so, you are insulting yourself.\"\n\t\t Bill Gates ")
print_function()
'''

# Task 2
'''
def strange_function(i):
   if(i % 2 == 0):
    print(i)

for i in range(1,20):
   if strange_function(i + 1):
      print(i % 2 == 0, end=' ')
'''

# Task 3
'''
def print_quadrate(lengh, symbol, number):
    if lengh == 7:
        for i in range(lengh):
                print(symbol * lengh)      

print_quadrate(7,'*',1)
'''

# Task 4
'''
def print_number(num):
    count = 0
    while num >= 0:
            count = count + 1


num1 = int(input("Введіть число: "))
print("There are:", print_number(num1))
'''
# Task 5

def print_number(number) -> bool:
    reversed_num = 0
    while number > 0:
        digit = number % 10         
        reversed_num = reversed_num * 10 + digit
        number = number // 10
        return number == reversed_num
    

print(print_number(394821))
print(print_number(421987))