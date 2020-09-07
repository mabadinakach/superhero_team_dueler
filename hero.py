import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):        
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    
    
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in. '''
        if len(self.abilities) > 0 and len(opponent.abilities) > 0:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                if opponent.is_alive() == False:
                    print(f"{self.name} won!")
                    opponent.add_death(1)
                    self.add_kill(1)
                    break
                self.take_damage(opponent.attack())
                if self.is_alive() == False:
                    print(f"{opponent.name} won!")
                    opponent.add_kill(1)
                    self.add_death(1)
                    break
        else:
            print("Draw")
            return

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self, incoming_damage):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        total_block = 0
        if len(self.armors) > 0:
            armor = random.choice(self.armors)
            print(f"Using: {armor.name}")
            total_block = incoming_damage - armor.block()
        else:
            print("You dont have any armor")
        return total_block

    def take_damage(self, damage):
        self.current_health -= damage

    def get_name(self):
        return self.name

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True 

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)
    
    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

