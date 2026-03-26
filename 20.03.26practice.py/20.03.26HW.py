# Task 1
'''
file_path = 'data.txt'

line1 = input("Write first line: ")
line2 = input("Write second line: ")
line3 = input("Write third line: : ")

with open("data.txt", "w") as f:
    f.writelines([line1,"\n",  line2,"\n", line3,"\n"])

    

# Task 2

with open("log.txt", "r") as f:
    text = f.read()
text = text.lower() 

for i in ",.!?;:-'\"":  
    text = text.replace(i, " ") 
words = text.split()


word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

top10words = []
used = []

for i in range(10):
    max_word = ""
    max_count = 0

for word in word_count:
        if word not in used and word_count[i] > max_count:
            max_count = word_count[word]
            max_word = word

if max_word != "":
        top10words.append((max_word, max_count))
        used.append(max_word)

with open("word_stats.txt", "w") as f:
    for word, count in top10words:
        f.write()
f.close()

'''

# Task 3


while True:
    try:
        print("============== Iнтернет-магазин ===============")
        print("| 1. Додати нове замовлення                   |")
        print("| 2. Переглянути всі замовлення               |")
        print("| 3. Пошук  замовлення за номером             |") 
        print("| 4. Оновити замовлення                       |")
        print("| 5. Видалити замовлення                      |")
        print("| 6. Вихід                                    |")
        print("===============================================")

        chose = input("Write (1-6): ")

        if chose == "1":
            order_num = input("Number of a order: ")
            product = input("Write name of the product: ")
            quantity = input("Write quantity: ")
            price = input("Write a price: ")

            with open('orders.txt', 'a') as f:
                f.write(f"{order_num}|{product}|{quantity}|{price}\n")
            print("Your order was added!")

        elif chose == "2":
            with open('orders.txt', 'r') as f:
                    lines = f.readlines()
            if not lines:
                print("File is empty!")
            elif found:
                    print("\n=== ALL ORDERS ===")
                    for line in lines:
                        print(line.strip())
                    print("==================")

        elif chose == '3':
            num = input("Number of order: ")
            with open('orders.txt', 'r') as f:
                lines = f.readlines()
                print(lines)
                found = False

        for line in lines:
            if  line.strip().startswith(num + "|"):
                print(line.strip())
                found = True
        if not found:
                print("Not found!")
    
        elif chose == '4':
            number = input("Write number of order to update it: ")
            new_quatity = input("New quatity: ")
            new_price = input("New price: ")
            with open('orders.txt', 'r') as f:
                lines = f.readlines()
                new_lines = []
                updated = False

            with open('orders.txt', 'w') as f:
                for line in lines:
                    if line.strip().startswith(number + '|'):
                        parts = line.strip().split("|")
                    new_line = (f"{parts[0]}|{parts[1]}|{new_quatity}|{new_price}\n")
                    f.write(new_line)
                    updated = True
                    print("The order was updated!")
                if not updated:
                    print("Order wasn't found!")

        elif chose == "5":
            num = input("Number of order to delete: ")
            new_lines = []
            deleted = False
            with open('orders.txt', 'r') as f:
                lines = f.readlines()

        for line in lines:
            if not line.strip().startswith(num + "|"):
                        new_lines.append(line)
            else:
                deleted = True
        with open('orders.txt', 'w') as f:
                    for line in new_lines:
                        f.write(line)
        if deleted:
            print("Order was deleted!")
        elif not found:
            print("Error, try again!")

        elif chose == "6":
            print("Quit.")
            break
        else:
            print("Error!")
            
    except FileNotFoundError:
        print("File is empty!")
    finally:
        input("END.")
