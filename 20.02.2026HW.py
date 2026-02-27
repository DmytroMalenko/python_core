# Task 1
'''
word = str(input("Write English word: "))

dictionary = {
    'Hello': 'Привіт',
    'House': 'Дім',
    'job': 'робота',
    'colleague': 'колега',
    'salary': 'зарплата',
    'contract': 'договір',
    'skills': 'навички',
    'office': 'офіс',
    'meeting': 'зустріч',
    'deadline': 'дедлайн ',
    'task': 'завдання',
    'training': 'навчання',
    'Chat': 'Чат',
    'How are you?': 'Як ти?',
    'Car': 'Машина',
    'Good bye': 'До зустрічі'
}

if word in dictionary:
        print(word,'—>', dictionary[word])
else:
    print("Erorr, wrong word or word with mistake.")

'''
# Task 2

text = str(input("Write play in which  your friends play together: "))
list1 = str(input("Do you want to see list of yours friends?: "))

friends = {
 'Friend1': {
    'Name': 'Anton',
    'Play': 'Fortnite'
    },
 'Friend2': {
     'Name': 'Vanya',
     'Play': 'Rust'
 },
 'Friend3': {
     'Name': 'Stas',
     'Play': 'Roblox'
 },
 'Friend4': {
     'Name': 'Kirill',
     'Play': 'Fortnite'
 },
 'Friend5': {
     'Name': 'John',
     'Play': 'Minecraft'
 },
 'Friend6': {
     'Name': 'Nikita',
     'Play': 'GTA 5'
 },
 'Friend7': {
     'Name': 'Roma',
     'Play': 'Minecraft'
 },
 'Friend8': {
     'Name': 'Maxim',
     'Play': 'Roblox'
 },
 'Friend9': {
     'Name': 'Timur',
     'Play': 'Rust'
 },
 'Friend10': {
     'Name': 'I(Dima)',
     'Play': 'Minecraft'
 }
}

Fortnite = {'Anton', 'Kirill'}
Minecraft = {'John', 'Roma', 'I(Dima)'}
Rust = {'Vanya', 'Timur'}
Roblox = {'Stas', 'Maxim'}
GTA_5 = {'Nikita'}

if list1 == 'Yes':
    print(friends)

if text == 'Fortnite':
    print(friends['Friend1']['Name'])
    print(friends['Friend4']['Name'])
elif text == 'Minecraft':
    print(friends['Friend5']['Name'])
    print(friends['Friend7']['Name'])
    print(friends['Friend10']['Name'])
elif text == 'Rust':
    print(friends['Friend2']['Name'])
    print(friends['Friend9']['Name'])
elif text == 'Roblox':
    print(friends['Friend3']['Name'])
    print(friends['Friend8']['Name'])
elif text == 'GTA_5':
    print(friends['Friend6']['Name'])
else: 
    print("Erorr")










