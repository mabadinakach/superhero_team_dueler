from ability import Ability
import random

class Weapon(Ability):

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        half_attack_damage = self.max_damage / 2
        return random.randint(half_attack_damage,self.max_damage)
        