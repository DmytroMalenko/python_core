
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return self.name + " " + self.surname

students = []
students.append(Student("Іван", "Петров"))
print("ТЕСТ 1:", students[0].name)    # Має: Іван
print("ТЕСТ 2:", students[0])         # Має: Іван Петров