from random import randint as r

from char_classes import LivingBeing


class Bard(LivingBeing):
    # def __init__(self):
    #     self.health = 40
    #     self.magic = 17
    #     self.attack_points = self.weapon.damage

    def super_attack(self, opponent: LivingBeing):
        """Casts stronger attack on enemy"""
        # print(f'This attack deals damage on {opponent}')
        damage = self.attack_points + r(7, 11)
        opponent.health -= damage
        self.magic -= 3
