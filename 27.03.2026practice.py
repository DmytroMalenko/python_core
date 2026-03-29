# Task 1
import turtle
'''
turtle.shape("turtle")
turtle.pensize(5)

# Квадрат
turtle.pencolor("red")
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.penup()
turtle.goto(-45,60)
turtle.forward(50)
turtle.right(90)
turtle.pendown()


# Рівносторонній трикутник
turtle.pencolor("green")
turtle.forward(80)
turtle.right(135)
turtle.forward(50)
turtle.right(85)
turtle.forward(50)
turtle.penup()
turtle.goto(300,100)
turtle.forward(50)
turtle.right(90)
turtle.pendown()

# П'ятикутник 
turtle.pencolor("blue")
turtle.right(50)
turtle.forward(90)
turtle.left(45)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(45)
turtle.forward(90)
turtle.left(90)
turtle.forward(120)
turtle.done()


# Task 2
turtle.shape("turtle")
turtle.pensize(5)
turtle.pencolor("black")

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.left(90)
turtle.forward(100)


turtle.pencolor("red")
turtle.begin_fill()
turtle.fillcolor('red')
turtle.right(60)
turtle.forward(60)
turtle.right(60)
turtle.forward(60)
turtle.end_fill()

turtle.penup()
turtle.goto(300,100)
turtle.pendown()
turtle.done()
'''


# Task 3
import random

colors = ["red","green", "blue", "purple", "black", "brown", "white,", "yellow", "orange", "gold", "gray," ]
turtle.shape("turtle")
turtle.pensize(5)
for _ in range(36):
    turtle.pencolor(random.choice(colors))

    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.left(10)

turtle.done()



















