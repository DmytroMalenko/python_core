# Tip dannich visnacha snacheni ta 

# intType = type(10)
#print(intType.__name__)
# print(type(intType))

'''
collection = list()
collection = []

print(type(collection)) # < class list >

items = [10, 12.3, 'text', True] # BAD PRACTICE

fruits = ['avocado', 'apple', 'orange', 'lemon', 'pear']

print(fruits[0])
print(fruits[1])
print(fruits[1:2])
print(fruits[:3])
print(fruits[2:])
print(fruits[1:4:2])
print(fruits[::2])

print(fruits[-1])
print(fruits[-1:-3:-2])
print(fruits[::-1])


#tring = 'text'
#string[2] = 'u'

print(fruits)
fruits[1] = 'mango' # apple -> mango
print(fruits)

fruits = ['avocado', 'apple', 'orange', 'lemon', 'pear']

fruits_count = len(fruits)
print(fruits_count)

counter = 0
while counter < len(fruits):
    print(fruits[counter], ' ')
    counter += 1

print()

for fruit in fruits:
    print(fruit, end= ' ')


names = input("Write lists of names: ")
print(type(names))
names = names.split()
print(type(names))
print(names)
names = ', '.join(names)
print(names)
print(type(names))


fruits = ['avocado', 'apple', 'orange', 'lemon', 'pear']

print(', '.join(fruits))

fruits.append('ananas')
print(', '.join(fruits))

fruits.extend(['mandarin', 'grapefruit'])
print(', '.join(fruits))

fruits.insert(4, 'mango')
print(', '.join(fruits))

fruits.pop(5)
print(', '.join(fruits))

fruits.append('Lemon')
print(', '.join(fruits))

fruits.remove('Lemon')
print(', '.join(fruits))

fruits.clear()
print(fruits)
print(len(fruits))



fruits = ['apple', 'mango', 'pamelo', 'pineapple', 'apple']

apple_count = fruits.count('apple')
print(apple_count)
mango_count = fruits.count('mango')
print(mango_count)
banana_count = fruits.count("banana")
print(banana_count)

pamelo_index = fruits.index("pamelo")
print(pamelo_index)

apple_index = fruits.index("apple")
print(apple_index)

#banana_index = fruits.index("banana") # ERORR
#print(banana_index) #Erorr

fruits_copy = fruits.copy()
fruits_copy.append("orange")
print(fruits_copy)
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print("apple")

if 'apple' in fruits:
    print("apple is a fruit")



list1 = [2,3,4]
list2 = [5,6,7]

result = list1 + list2
print(result)
print(result * 3)


numbers = [10, 3, -5, 0, 0, 9, -10, 12, 1]
even_numbers = [x * 10 for x in numbers if x % 2== 0]
print(even_numbers)

odd_numbers = [x for x in range(1,20,2)]
print(odd_numbers)



fruits = ['apple', 'mango', 'pamelo', 'pineapple', 'apple']

fruits_tuple = tuple(fruits)
print(fruits_tuple)
print(type(fruits_tuple))
#fruits_tuple.remove("apple")
#fruits_tuple[3] = 'kiwi'
print(fruits_tuple)

fruits_tuple = ('kiwi', 'pamelo')

list2d = [ [1,2,3], 
          [4,5,6]
]

print(list2d[0])
print(list2d[0][1])

for i in list2d:
    for j in i:
        print(j, end= ' ')
        print()
'''


fruits = ['apple', 'mango', 'pamelo', 'pineapple', 'apple']

colors = ('red', 'green', 'blue', 'pink')

(red, green, blue, pink) = colors

print(red)
print(green)
print(blue)
print(pink)

(red, green, *other_colors) = colors
print(red)
print(green)
print(other_colors)





