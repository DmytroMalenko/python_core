# Task 1
'''
def print_function():
    print("\"Don't let the noise of others' opinions\n\tdrown out your own inner voice.\"\n\t\t Steve Jobs ")
print_function()
'''

# Task 2
'''
def strange_function(i):
   if(i % 2 != 0):
    print(i)

for i in range(1,20):
   if strange_function(i + 1):
      print(i % 2 != 0, end=' ')
'''

# Task 3
'''
side = 'vertikal'
side1 = 'horisontal'

def print_funktions(long, side, symbol):
        
        if side == 'vertikal':
            for i in range(long):
                print(symbol)

        elif side == 'horisontal':
            print(symbol * long)

print_funktions(10, 'vertikal', '*')
print()
print_funktions(10, 'horisontal', '*')
'''

# Task 4
'''
def print_sum(a,b,c,d):
    if a > b and a > c and a > d:
        print(a)
    elif b > a and b > c and b > d:
        print(b)
    elif c > a and c > b and c > d:
        print(c)
    elif d > a and d > b and d > c:
        print(d)

print_sum(1000,2003,590,-7)
'''

# Task 5
'''
def print_num(a):
    if a % 2 == 0:
        return False

print_num(7)
'''

# Task 6
def numbers(a,b,c,d,e,f) -> bool:
    first_sum = a + b + c
    second_sum = d + e + f
    if first_sum == second_sum:
        return False
print(numbers(1,2,3,4,2,0))

