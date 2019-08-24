from char_classes import LivingBeing


class Mage(LivingBeing):

    def fire_spell(self, opponent: LivingBeing):
        """Casts stronger damage on enemy"""
        # print(f'This spell casts damage on {opponent}')
        damage = self.magic + self.attack_points
        opponent.health -= damage
        self.magic -= 3
