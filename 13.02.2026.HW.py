# Task 1
'''
text = int(input("Write how many cells you want to go to the right?: "))

list1 = list()
list1 = [1,2,3,4,5]

if text == 1: 
    print(list1[4],[1],[2],[3],[4])
elif text == 2: 
    print(list1[3],[5],[1],[2],[3])
elif text == 3: 
    print(list1[2],[4],[5],[1],[2]) 
elif text == 4: 
    print(list1[1],[3],[4],[5],[1])
elif text == 5:
    print(list1[::-1])
else:
    print("Erorr, write 1-5.")
'''
# Task 2
list1 = [30,4,2,9,8]
list2 = [18,4,7,2,6]
list3 = []

# ● Сформувати третій список, що містить елементи обох списків;
'''
list3 =  list1 + list2
print(list3)
'''

# ● Сформувати третій список, що містить елементи обох списків без повторень;
'''
for i in list1:
    if i not in list2:
        list3.append(i)
        print(list3) 

for i in list2:
    if i not in list1:
        list3.append(i)
        print(list3) 
    '''

# ● Сформувати третій список, що містить елементи спільні для двох списків;
'''
for i in list1:
    if i in list2 and i not in list3:
        list3.append(i)
print(list3)

'''

# Сформувати третій список, що містить тільки унікальні елементи кожного зі списків;
'''
for i in list1:
    if i not in list2:
        list3.append(i)

for i in list2:
    if i not in list1:
        list3.append(i)

print(list3)
'''

# ● Сформувати третій список, що містить тільки мінімальне і максимальне значення кожного зі списків.

for i in list1:
    if i != list1:
        print(i)

print()

for i in list2:
    if i != list2:
        print(i)


