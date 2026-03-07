# Task 1
'''
def summa(a: int, b: int):
    if b == 0:
        return a
    else:
        print(f"{a} % {b} = {a % b}")
        return summa(b, a % b)

print(summa(12, 36))
print()
print(summa(8, 10))


# Task 2

def summa(a: float, b: float, c: float):
    if c == 0:
        return a
    else: 
        print(f'{a} + {b} + {c} = {a+b+c}')

print(summa(1,2,3))
'''

# Task 3

num = [1,2,3,2,1]

def summa(a1,b1,c,a2,b2):
    if a1 and b1 == a2 and b2:
        print(f'{a1} + {b1} = {a1 + b1}')
        print(f'{a2} + {b2} = {a2 + b2}')
    else:
        print("Error")
print(summa(4,4,8,4,4))












