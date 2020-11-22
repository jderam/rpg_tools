import random
import dice
from maze_rats_data import abilities, abilities2, gender, features, items, \
    light_weapons, heavy_weapons, ranged_weapons, \
    appearances, physical_details, backgrounds, clothing, personalities, mannerisms


class PlayerCharacter:

    def __init__(self,
                abilities_method=1,
                ):
        self.abilities_method = abilities_method
        if self.abilities_method == 1:
            self.abilities = random.choice(abilities)
        elif self.abilities_method == 2:
            self.abilities = []
            for i in range(3):
                self.abilities.append(abilities2[dice.roll_dice(1,6)])
        self.hp = 4
        self.gender = random.choice(gender)
        self.atk_bonus = 0
        self.spell_slots = 0
        self.feature_roll = dice.roll_dice(1,6)
        if self.feature_roll == 1:
            self.atk_bonus += 1
        elif self.feature_roll == 2:
            self.spell_slots += 1
        else:
            pass

        self.feature = features[self.feature_roll]
        self.equipment = random.sample(items, k=6)
        self.armor = 'Light Armor (AC 6)'
        self.ac = 6
        self.weapons = random.sample(light_weapons + heavy_weapons + ranged_weapons, k=2)
        self.appearance = random.choice(appearances)
        self.physical_detail = random.choice(physical_details)
        self.background = random.choice(backgrounds)
        self.clothing = random.choice(clothing)
        self.personality = random.choice(personalities)
        self.mannerism = random.choice(mannerisms)


    def to_dict(self):
        char_dict = self.__dict__
        return char_dict


if __name__ == '__main__':
    from pprint import pprint
    my_pc = PlayerCharacter()
    pprint(my_pc.to_dict())
