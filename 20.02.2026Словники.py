#Task 1
'''
discard = str(input("Write name which is in contacts if you want to delete it: "))
add1 = str(input("Write name which do you want to addd in contacts: "))
look_throuth = str(input("Do you want to see all your contacts?: "))
contatcs = {'Anton', "Katya"}

contatcs.add(add1)
print(', '.join(contatcs))


contatcs.discard(discard)
print(', '.join(contatcs))

if look_throuth == 'Yes':
    print(contatcs)
else: 
    print("Error, you don't have this name or name has symbols.")



# Task 2

text = str(input("Write text: "))

all_text = {text}
count = 0

if text in all_text:
    count += 1



# Task 3

rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

money = str(input("Write USD or EUR or PLN: "))
money1 = float(input("Write prise at Hryvnias: "))


if money == 'USD':
    print(f' {money1} / 40.2 = {money1 / 40.2}''$')
elif money == 'EUR':
    print(f' {money1} / 42.5 = {money1 / 42.5}''€')
elif money == 'PLN':
    print(f' {money1} / 9.6 = {money1 / 9.6}''₮')
else: 
    print("Error")

'''

# Task 4 

word = str(input("Write English word: "))

dictionary = {
    'Hello': 'Привіт',
    'Chat': 'Чат',
    'How are you?': 'Як ти?',
    'Car': 'Машина',
    'Good bye': 'До зустрічі'
}

if word in dictionary:
        print(word,'—>', dictionary[word])
else:
    print("Erorr, wrong word or word with mistake.")



