
employees = {
    'Emploee1' : {
        'Name' : 'Maria',
        'Position' : 'Content Manager',
        'Salary' : 34000
    },
    'Emploee2' : {
        'Name' : 'Anton',
        'Position' : 'Content Manager',
        'Salary' : 67000
    },
    'Emploee3' : {
        'Name' : 'Anastasia',
        'Position' : 'Content Manager',
        'Salary' : 67000
    }
}

print(employees['Emploee3']['Name'])


'''
my_set = set()
my_set = set(['apple', 'orange', 'cherry'])

food = ['apple', 'orange', 'cherry']

# print('cherry' in food)

my_set = {'apple', 'orange', 'cherry', 'mango'}
my_set2 = {'mango', 'pepper', 'apple', 'kiwi'}

contacts = {
    'Anton' : '095098209582',
    'Anastasiya': '920840821091',
    'Sergei': '902834018389377'
}

print(contacts['Anton'])
contacts['Anastasiya'] = '04956ß9592095'
print(contacts['Anastasiya'])
contacts['Kirill'] = '048328290358208'
print(contacts['Kirill'])

contacts_copy = contacts
contacts_copy['Taras'] = 'ß3940342091'
print(contacts['Taras'])


for value in contacts.values():
    print(value)

for key in contacts.keys():
    print(key)

for key in contacts:
    print(f'{key}: {contacts[key]}')

for pair in contacts.items():
    print(f'{pair[0]}: {pair[1]}')

contacts.update({'Katya' : '0489572972506'})
contacts.update([('Katya', '0303830840291'), ('Timofiy', '4985808098')])
print(contacts['Katya'])


contacts.pop('Anton')
print(contacts)
contacts.popitem()
print(contacts)
contacts.clear()
print(contacts)

new_ditionary = dict()
new_ditionary = {
    'key' : 'value',
    10 : 12.3
}
print(new_ditionary)
print(type(new_ditionary))



frozen_fruits = frozenset(my_set | my_set2)
print(', '.join(frozen_fruits))
print(type(frozen_fruits))


my_set.symmetric_difference_update(my_set2)
print(my_set)

sym_difference = my_set.symmetric_difference(my_set2)
sym_difference = my_set ^ my_set2
print(sym_difference)


my_set.difference_update(my_set2)
print(my_set)

difference = my_set.difference(my_set2)
difference = my_set - my_set2
print(difference)


my_set.intersection_update(my_set2)
print(my_set)

intersect = my_set.intersection(my_set2)
intersect = my_set & my_set2
print(intersect)

union = my_set.union(my_set2)
union = my_set | my_set2
print(union)

# print(my_set[0])

#print(my_set)
#print(type(my_set))

#print(len(my_set))

new_set = {True, 1, 0, False}
'''
#print(new_set)

my_list = ['apple', 'cherry', 'orange']

'''
for item in my_set:
    print(item)

print('apple' in my_set)
print('banana' not in my_set)

#counter = 0
#while counter < len(my_list):
#   print()

print(', '.join(my_set))
my_set.add('banana')
print(', '.join(my_set))
my_set.update(['mango', 'kiwi'])
print(', '.join(my_set))

my_set.remove('apple')
print(', '.join(my_set))
my_set.discard('banana')
print(', '.join(my_set))
my_set.pop()
print(', '.join(my_set))
my_set.clear()
print(', '.join(my_set))
'''









