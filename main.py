from characters import *
from enemies import *

# Enemies
grob = Goblin("Glob", 10, 30)
dracula = Vampire("Dracula", 12, 40)

# Players
boris = Fighter("Boris", 15, 50)
anna = Healer("Anna", 7, 35)

print("--- Stats before fight ---")
print(grob, dracula, boris, anna, sep='\n')

# Enemies turn
grob.attack(boris)
dracula.attack(boris)

# Players turn
boris.attack(dracula)
anna.heal(boris)

# Enemies turn
grob.attack(anna)
dracula.life_steal(anna)

print("--- Stats after fight ---")
print(grob, dracula, boris, anna, sep='\n')