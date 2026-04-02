# Task 1

import random
import string


print("1 - Add random number to your nick name.")
print("2 - Add (_,.-) and 3 random letters. (vlad_xqp)")
print("3 - Make first letter big and add random Prefix (Pro, SUper, Ultra) and mix your nick name with 2 random numbers")

name = input("Write your nick name for programm: ").strip()

choice = input("Write (1-3): ")

'''
if choice == '1':
    nickname = name + str(random.randint(100,9999))
    print(nickname)


if choice == '2':
    choice1 = random.choice(['_', ',', '.', '-'])
    letters = ''.join(random.choices(string.ascii_lowercase, k=3))
    nickname = name + choice1 + letters
    print(nickname)

    
if choice == '3': 
    prefixes = ['Pro', 'Super', 'Ultra']
prefixes = random.choice(prefixes)

upper1 = name[0].upper() + name[1:]

num = str(random.randint(10,99))
nickname = upper1 + prefixes + num
print(nickname)

'''




















































































