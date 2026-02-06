'''
# int str float bool range type

string = str()

for i in range(4,10,3):

number = input("Write number: ")
print(type(number))

#       012345
text = 'Hello, World'
print(text[0])
print(text[4])
print(text[49])

 text[start:and:step]
 0:5 == :5
print(text[3:])
print(text[0:5])
print(text[2::2])
print(text[::2])

print(text[-2])
print(text[-4:-9:-2])
print(text[::-1])

text[4] = 'U' # ERROR

print(len(text))
print(text[6])
length =len(text)
print(length)

text = 'Hello, World!'

if text.startswith("Hello"):
    print("This text - it's welcome")


if text.endswith("!"):
    print("This text - it#s report")


text = text.strip()
print(text.split(" , "))
print(text)

text_modified = text.replace('World', 'Python')
print(text_modified)
print(text)
text_upper = text.upper()
text_lower = text.lower()
print(text_upper)
print(text_lower)
print(text)

str1 = 'Hello'
str2 = 'Python'

result = str1 + ',  ' + str2
print(result)
print(str1 * 4)

counter = 0
while counter < len(text):
    print(text[counter], end= ' ')
    counter += 1

for symbol in text:
    print(symbol, end= ' ')

if 'a' in 'apple':
    print("a is in apple")

if 'Hello' in 'Hello World':
    print("hello is in text")
else:
    print("hello is not in text")

print("A" < 'a')
print("lemon" > 'apple')
print("blue" > 'red')

fruit = input("Write name of fruit: ")
if fruit == 'apple':
    print("Fruit is apple")

'''
message = 'Hello World'

encoded  = message.encode("UTF-16")
print(encoded)
print(message.encode("UTF-16"))






