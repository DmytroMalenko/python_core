'''
def print_contact(contact):
    if contacts[key]['mobile'] != None: print(f'\ttmobile: {contacts[key]['mobile']}')
    if contacts[key]['mobile'] != None: print(f'\tworknum: {contacts[key]['worknum']}')

contacts = {
    'Anya': {
    'Mobile': '3084922983',
    'Worknum': '09489285'
},
    'Anton STO': {
    'Mobile': None,
    'Number': '092850194'
},
    'Timofi Karpati': {
    'Mobile': '0849283',
    'Number': None
},
}

print("1. Look through all contacts\n2. Find contact\n0. Quit")
action = int(input("Choose way: "))

while action != 0:
    match action:
        case 1:
            for key in contacts:
                print(key)
                print_contact(contacts[key])
        case 2:
            name = input("Write name: ")
            if name in contacts:
                print_contact(contacts[name])
            else:
                print("Erorr")
        case _:
            print("Erorr")
    print("1. Look through all contacts\n2. Find contact\n0. Quit")
action = int(input("Choose way: "))


def print_greeting():
    print("======================")
    print("==== Hello, User! ====")
    print("======================")

def print_named_greeting(name: str = 'guest'):
    print("======================")
    print(f"==== Hello, {name.upper()}! ====")
    print("======================")

print_named_greeting()
print_named_greeting("Anton")
# print_greeting()


def my_sum(num1: float, num2: float) -> float:
    return num1 + num2


result = my_sum(10,12)
print(result)



def print_full_name(first_name: str, last_name: str):
    print(f"{last_name} {first_name}")

print_full_name(last_name= 'Malenko', first_name='Dmytro')
print_full_name('Dmytro', 'Malenko')



def print_my_animal(animal,name, age):
    print(f"I have {animal} {age} years old named {name}.")

print_my_animal('dog', age = 10, name = 'Patron')



def only_positional(name, /):
    print("Hello, " + name)

#only_positional(name= 'Vova')

def only_key_word(*, name):
    print("Hello " + name)

only_key_word(name='Vova')

print("data", 10, 'abc', sep=', ', end='!!!!!!!')

def my_sum(*nums):
    result = 0
    for i in nums:
        result += i 
        return result
    
print(my_sum(10,12,12))
print(my_sum(10,12))
print(my_sum(210))
print(my_sum(10,10,10,10,10,10,10,10,10,10,10,10,10,10))



def my_function(**data):
    print(type(data))
    for key in data:
        print(f'{key}: {data[key]}')

my_function(name='Vova', city='Odesa', job='Teacher')



def unpack_list(a,b,c):
    print(a,b,c, sep=', ')

my_list = [4,5,6]
unpack_list(*my_list)

def unpack_dictionary(fname, lname):
    print(fname,lname)

person = {
    'fname': 'Anton',
    'lname': 'Koval'
}

unpack_dictionary(**person)



global_var = 16
def local_function(local_param):
    global global_var
    global_var = 10
    local_var = 10
    print(local_param, local_var, global_var)

local_function(5)
print(global_var)




def enclosing_func():
    enclosing_var = 10
    def inner_func():
        print("Hello from inner", enclosing_var)
    inner_func()

enclosing_func()



def do_something():
    print("Doing some stuff...")

def main():
    print("Start programm...")
    do_something()
    print("End of programm.")

if __name__ == '__main__':
    main()

'''


