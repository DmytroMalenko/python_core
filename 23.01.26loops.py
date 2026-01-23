#needed_potates = int (input("Wrote how many potates do you need: "))
#peeled_potates = 0

#while peeled_potates < needed_potates:
   # print("Take potates")
   # print("Do potates")
   # print("Ready!")                                                                                                                                                                                                                                                                                                                                                                                                                  
   # peeled_potates += 1

# print(f'{peeled_potates} potates was do')

'''
while True:
 num1 = float(input("Write first number: "))
 num2 = float(input("Write second number: "))
 action = input("Chose (+,-,*, /): ")

 match action:
    case '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    case '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    case '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    case '/':
        if num2 == 0:
            print("You cant / 0!")
        else: 
            print(f'{num1} / {num2} = {num1 / num2}')
    case _:
        print("not correct")
 q = input("Write q to quit: ")
 if q == 'q':
     break

     '''

needed_potates = int (input("Wrote how many potates do you need: "))
peeled_potates = 0

while peeled_potates < needed_potates:
    print("Take potates")
    is_rotten = input("Potatoes isnt good?")
    if is_rotten == 'yes':
        print("Dont take!")
        continue
    print("Do potates")
    print("Ready!")                                                                                                                                                                                                                                                                                                                                                                                                                  
    peeled_potates += 1
    is_tired = input("Are you tired?")
    if is_tired == 'yes': 
        break
print(f'{peeled_potates} potates was do')

