class Fighter:
    def __init__(self, name, damage, hp) -> None:
        self.name = name
        self.damage = damage
        self.hp = hp

    def attack(self, target):
        print(f'Fighter {self.name} attacks {target.name}')
        target.hp -= self.damage

    def __str__(self):
        return f'Name: {self.name}\n\tDamage: {self.damage}\n\tHealth {self.hp}'

class Healer: 
    def __init__(self, name, heal_amount, hp) -> None:
        self.name = name
        self.heal_amount = heal_amount
        self.hp = hp

    def heal(self, target):
        print(f'Healer {self.name} heals {target.name}')
        target.hp += self.heal_amount

    def __str__(self):
        return f'Name: {self.name}\n\tHeal amount: {self.heal_amount}\n\tHealth {self.hp}'