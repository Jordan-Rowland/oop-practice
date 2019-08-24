from typing import List


class LivingBeing:

    items = List[str]

    def __init__(self, name: str, weapon: str):
        self.name = name
        self.weapon = weapon
        self.health = 30
        self.magic = 20
        self.attack_points = 3

    def attack(self, opponent):
        damage = self.attack_points + r(3, 7)
        opponent.health -= damage






class Item:
    def __init__(self, item_type: str):
        self.item_type = item_type

    def use_item(self, recipient: LivingBeing):
        if self.item_type.lower() == 'potion':
            recipient.health += 5
        if self.item_type.lower() == 'mana':
            recipient.magic += 5
