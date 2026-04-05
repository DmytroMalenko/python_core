class Animal: 
    def __init__(self, name, type, sound) -> None:
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        print("animal makes some sound")
    
    def make_sound(self):
        print(f"Animal of type {self.type} named {self.name} make sound: {self.sound}")

    def __str__(self) -> str:
        return f"Name: {self.name}\nType: {self.type}\n Sound: {self.sound}"



animal = Animal("Buddy", 'dog', 'woof')
animal2 = Animal("Charlie", 'parrot', 'hello')

print(animal)
animal.make_sound()
animal2.make_sound()
#animal.type = 'dog'
#print(animal2.type)
#print(animal.type)
#print(type(animal))

'''
class Calcucator: 
    def add(self, num1, num2):
        return num1 + num2
    
    def subtruct(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0: raise ZeroDivisionError()
        return num1 / num2
    

calc = Calcucator()
print(calc.add(10,12))
print(calc.multiply(5,5))

'''






