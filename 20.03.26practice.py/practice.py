
# Task 1
'''
file_path = 'data.txt'
with open("data.txt", "r") as f:
        text = f.read()
with open("backup.txt", "w") as f:
        f.write(text)


# Task 2

with open("data.txt", "r") as f:
    text = f.read()
result = ''
for number in text:
    if number == "a":
        result = result + "b"
    elif number == "b":
        result = result + "c"
    elif number  == "c":
        result = result + "d"
    elif number == "d":
        result = result + "e"
    elif number == "e":
        result = result + "f"
    elif number == "f":
        result = result + "g"
    elif number == "g":
        result = result + "h"
    elif number  == "h":
        result = result + "i"
    elif number  == "i":
        result = result + "j"
    elif number  == "j":
        result = result + "k"
    elif number  == "k":
        result = result + "l"
    elif number  == "l":
        result = result + "m"
    elif number  == "m":
        result = result + "n"
    elif number  == "n":
        result = result + "o"
    elif number  == "o":
        result = result + "p"
    elif number  == "p":
        result = result + "q"
    elif number  == "q":
        result = result + "r"
    elif number  == "r":
        result = result + "s"
    elif number  == "s":
        result = result + "t"
    elif number  == "t":
        result = result + "u"
    elif number  == "u":
        result = result + "v"
    elif number  == "v":
        result = result + "w"
    elif number  == "w":
        result = result + "x"
    elif number  == "x":
        result = result + "y"
    elif number  == "y":
        result = result + "z"
    elif number  == "z":
        result = result + "a"
    else:
        result = result + number


with open("encrypted.txt", "w") as f:
    f.write(result)

'''
# Task 3^


while True:
    try:
        print("============== МЕНЮ ===============")
        print("| 1. Додати новий альбом          |")
        print("| 2. Переглянути всю колекцію     |")
        print("| 3. Пошук альбомів за виконавцем |") 
        print("| 4. Видалити альбом              |")
        print("| 5. Вихід                        |")
        print("===================================")

        chose = input("Write (1-5): ")

        if chose == "1":
            name = input("Name of album: ")
            performer = input("Performer: ")
            year = input("Year of production: ")
            with open('music_collection.txt', 'a') as f:
                f.write(f"{name}|{performer}|{year}\n")
            print("Album was added!")

        elif chose == "2":
            with open('music_collection.txt', 'r') as f:
                lines = f.readlines()
                print(lines)
        else: 
            print("Collection is empty!")

        if chose == '3':
            performer = input("Name of performer: ")
            with open('music_collection.txt', 'r') as f:
                text = f.read()
                lines = text.split('\n')
        for line in lines:
            if '|' in line and performer.lower() in line.lower():
                print(f"{line.strip()}")
        else: 
            print("Not found!")
    
        if chose == '4':
            name = input("Name of album to delete: ")
            with open('music_collection.txt', 'r') as f:
                lines = f.readlines()
                new_lines = []

        for line in lines:
            album_name = line.strip().split('|')[0]
        if album_name.lower() != name.lower():
                new_lines.append(line)

        if chose == "5":
            print("Quit.")
        break
    except FileNotFoundError:
        print("File is empty!")

    finally:
        input("END.")





