# Task 1
'''
str1 = str(input("Write some text: "))
count = 0

for i in str1:
    if i == '.':
        count += 1
    elif i == '?':
        count += 1
    elif i == '!':
        count += 1
    elif i == ';':
        count += 1
print("There are", count)


# Task 2

text = str(input("Write a palindrome: "))

if text == text[::1]:
    print("It's palindrome")
elif  text != text[::1]:
    print("Erorr, it isn't palindrome")



# Task 5

text = str(input("Write some text: "))
symbols = str(input("Write symbols (§,$,%,&,/,?,*,~,@,.,,,!): "))

if symbols == '§':
    text_modified1 = text.replace('§', ' ')
    print(text_modified1)
 
elif symbols == '$':
    text_modified2 = text.replace('$', ' ')
    print(text_modified2)

elif symbols == '%':
    text_modified3 = text.replace('%', ' ')
    print(text_modified3)

elif symbols =='&':
    text_modified4 = text.replace('&', ' ')
    print(text_modified4)

elif symbols == '?':
    text_modified5 = text.replace('?', ' ')
    print(text_modified5)
  
elif symbols == '*':
    text_modified6 = text.replace('*', ' ')
    print(text_modified6)
 
elif symbols == '~':
    text_modified7 = text.replace('~', ' ')
    print(text_modified7)

elif symbols == '@':
    text_modified8 = text.replace('@', ' ')
    print(text_modified8)

elif symbols == '.':
    text_modified9 = text.replace('.', ' ')
    print(text_modified9)
       
elif symbols == '!':
    text_modified10 = text.replace('!', ' ')
    print(text_modified10)

elif symbols == ',':
    text_modified11 = text.replace(',', ' ')
    print(text_modified11)

    '''

# Task 6

text = str(input("Write some text: "))

word = text.split() 
i = len(word) - 1

while i >= 0:
    print(word , end= ' ')
    i -= 1