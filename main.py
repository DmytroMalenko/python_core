'''
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
print(grob, dracula, boris, anna, sep='\n'



import cowsay 
# cowsay.cow("Hello!")
cowsay.octopus("Hello, I am octopus")
cowsay.trex("RAAAAAAAAAAAAA")


from art import *
tprint("Hello")

art_text = textZart("Hello", font= 'block', chr_ignore = True)
print(art_text)

tprint("test", "rnd-xlarge")
'''

from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="List of Students")
table.add_column("Name", style="cyan")
table.add_column("Prolekt", style="magenta")
table.add_row("Anton", "Chat-Bot")
table.add_row("Maria", "Play on Python")

console.print(table)



