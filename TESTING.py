import string
import random

s = ''.join(random.choice(string.printable) for _ in range(20))
print(s)

