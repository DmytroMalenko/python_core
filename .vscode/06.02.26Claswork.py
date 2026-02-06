# Task 1
'''
str1 = str(input("Write something: "))
print(len(str1))



# Task 2
text = input("Write something:  ")
symbol = input("Enter symbol: ")
count = 0

for i in text:
    if i == symbol:
        count+= 1
    print(f'Symbol {symbol} is {count} times')

# Task 3

str1 = str(input("Write something: "))
str2 = str(input("Write something: "))

str1 = str1.replace(str1, str2)
str2 = str2.replace(str2, str1)
print(str2)
print(str1)



# Task 4

text = input("Write something: ")
word = input("Wirte word to search: ")
count = 0

for i in text: 
    if word == text:
        count += 1
        print(count)

'''

# Task 6

text = input("Write something: ")
longest = ""
for i in text.split():
    if len(i) > len(longest):
        longest = i
        print(longest)