# Task 1
class Student: 

    def __init__(self, name, surname, age, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.marks = marks

    def __str__(self):
        return f'Name: {self.name}\n\tSurname: {self.surname}\n\tAge: {self.age}\n\tMarks: {self.marks}'

    def all_marks(self):
        print(f"Here is all marks from {self.surname} {self.name}:\n{self.marks}")


    def marks_add(self, mark):
        self.marks.append(mark)
        print(f"Mark {mark} was added!")



class Car: 
    def __init__(self, brand, model, speed, year) -> None:
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def __str__(self):
        return f'Brand: {self.brand}\n\tModel: {self.model}\n\tSpeed: {self.speed}\n\tYear: {self.year}'
    
    def info(self):
        print(f"{self.__str__}")
    































