'''
from students_and_cars import *
students = []
cars = []

found = False

print("<--------------------- MENU -------------------->")
print("1. All Students and their information           |")
print("2. Add Student                                  |")
print("3. Delete Student                               |")
print("4. Add mark                                     |")
print("5. All cars                                     |")
print("6. Add car                                      |")
print("7. Exit                                         |")
print("-------------------------------------------------")


while True: 


    choice = input("Write (1-7):")

    if choice == '1':
        for i in range(len(students)):
            print(f"{students[i]}")


    elif choice == '2' and True:
        name = input("Name: ")
        surname = input("Surname: ")
        age = int(input("Age: "))
        marks = [int(input("Marks: "))]  
        student = Student(name, surname, age, marks)
        students.append(student)
        print("Student was successfully added in the list!")

    elif choice == "3": 
        name = input("Name: ")
        surname = input("Surname: ")

        for i in students: 
            if i.name and i.surname == name and surname:
                students.remove(i)
                print("Student deleted.")
                break
            elif not students:
                print("This student isn't in Menu!")


    elif choice == "4":
        name = input("Name: ")
        surname = input("Surname: ")
        marks = input("Mark: ")

        for s in students:
            if s.name == name and s.surname == surname:
                marks.append(marks)
                print("Mark added.")
                break
    
    elif choice == "5":
        for i in range(len(cars)):
            print(f"{cars[i]}")

    elif choice == "6":
        brand = input("Brand: ")
        model = input("Model: ")
        speed = input("Speed(km/h): ")
        year = input("Year: ")
        car = Car(brand, model, speed, year)
        cars.append(car)
        print("Car was added!")

    elif choice == "7":
        break
    '''

# Task 2
import math 

class Circle: 

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius * self.radius) 
    
    def perimetr(self):
        return 2 * math.pi * self.radius

class Triangle: 
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def perimetr(self):
        return self.a + self.b + self.c
    

class Rectangle: 
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimetr(self):
        return 2 * (self.length + self.width)
    
while True:
    def menu():
        print("======== MENU ========")
        print("1. Circle            |")
        print("2. Triangle          |")
        print("3. Rectangle         |")
        print("4. Exit              |")
        print("======================")
    choice = input("Which figure do you need?(1-4):")

    if choice not in  ("1","2","3","4"):
            print("Error incorecct number.(1-4)")


    elif choice == "1":
            radius = float(input("Write radius: "))
            circle = Circle(radius)
            print("Area:", circle.area(),"cm")
            print("Perimetr:", circle.perimetr(),"cm")

    elif choice == "2":
            a = float(input("Write a(in cm): "))
            b = float(input("Write b(in cm): "))
            c = float(input("Write c(in cm): "))
            triangle = Triangle(a, b, c)
            print("Area:", triangle.area(),"cm")
            print("Perimetr:", triangle.perimetr(),"cm")
    
    elif choice == "3":
            length = float(input("Write length: "))
            width =  float(input("Write width: "))
            rectangle = Rectangle(length, width)
            print("Area:", rectangle.area(),"cm")
            print("Perimetr:", rectangle.perimetr(),"cm")

    elif choice == "4":
        break
        
    menu()