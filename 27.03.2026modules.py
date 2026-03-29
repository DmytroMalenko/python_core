import random
'''
# from random import *

print(random.randint(10,14))
print(random.randrange(10,18, 2)) # 10 12 14

# print(random())
#if random() > 0.5:
#    print('heads')
#else:
#    print("tails")

print(random.uniform(10.5, 20.6))

fruits = ['apple', 'banana', 'orange', 'pineapple', 'mango']

print(random.choice(fruits))
print(random.choice('apple'))
weights = [0.1, 0.5, 0.1, 0.1, 0.2]
print(random.choices(fruits, weights=weights, k=3))

print(random.sample(fruits, k=4))

fruits.sort()
print(fruits)
random.shuffle(fruits)
print(fruits)
'''
import math
'''
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)


number = 10.5
print(math.ceil(number)) # 11
print(math.floor(number)) # 10
print(math.trunc(number)) # 10
print(math.fabs(number)) # modul
print(math.sqrt(4)) # square root 
print(math.sqrt(9))

print(math.pow(1.5, 2))
print(math.pow(2, 0.5))

print(math.log(12, 2))
print(math.log10(100))

print(math.factorial(5))
print(math.gcd(10,15))



import string

print(string.ascii_letters)
print(string.ascii_letters)
print(string.ascii_letters)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)

print(string.punctuation)
print(string.printable)
print(string.whitespace)
'''

import turtle
import time
'''
turtle.shape('turtle')
turtle.pensize(5)
turtle.pencolor((0.5, 0.3, 0.9))
turtle.colormode(255)
print(turtle.pencolor())
turtle.pencolor(125, 75, 230)
# turtle.pencolor('#32c18f') # RGB

screen = turtle.Screen()

screen.onkey(lambda: turtle.forward(15), 'w')
screen.onkey(lambda: turtle.right(5), 'd')
screen.onkey(lambda: turtle.left(5), 'a')
screen.onkey(lambda: turtle.back(15), 's')

screen.onclick(lambda a,b: turtle.goto(a,b))
screen.listen()
'''

import my_module 
my_module.greeting
turtle.speed(my_module.turtle_settings['shape'])
turtle.pensize(my_module.turtle_settings['pensize'])
turtle.pencolor(my_module.turtle_settings['pencolor'])
turtle.fillcolor(my_module.turtle_settings['fillcolor'])






'''
#turtle.delay()
# turtle.speed('slowest')
#turtle.delay(100)
# time.sleep(1)
turtle.forward(100)
turtle.pencolor('red')
turtle.left(90)
turtle.back(100)
turtle.pencolor('blue')
turtle.right(90)
turtle.circle(55)

turtle.penup()
turtle.goto(-45,60)
turtle.pendown()
turtle.fillcolor('purple')
turtle.begin_fill()
turtle.circle(34)
turtle.end_fill()
'''
turtle.done()








