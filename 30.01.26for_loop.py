#print(range(10)) # 0 1 2 3 4 5 6 7 8 9
#print(range(3,8)) # 3 4 5 6 7 
#print(range(4,11,3)) # 4 7 10
#r = range(5)
#print(type(r).__name__)
#print(type(10).__name__)

#counter = 0
#while counter < 5:
#    print(counter, end= ' ')
 #   counter += 1

# 0 1 2 3 4 
#for i in range(5):
 #   print(i, end= ' ')

'''
for i in range(3): 
    print(i)
    for j in range(5):
        print(j, end= ' ')
    print()

print("For: ")

count = int(input(" Write "))
r = range(count)
for i in r: 
    print(i)



print("While: ")
counter_outer = 0
while counter_outer < 3:
    print(counter_outer)
    counter_outer = 0
    while counter_outer < 5:
        print(counter_outer, end= ' ')
        counter_outer += 1
    print()
    counter_outer += 1

'''

import random # iport all modyl
randint = 10
random_number  = random.randint(0,15)
print(random_number)

from random import randint
randint  = 10
print(randint(0,10))



