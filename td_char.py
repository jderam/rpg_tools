import random
from copy import deepcopy
from td_data import (
    races,
    traits,
    adventurers_kit,
    weapon_proficiencies,
    light_weapons,
    heavy_weapons,
    ranged_weapons,
)


class PlayerCharacter:
    def get_traits(self):
        rand_traits = {}
        if "RANDOM" in races[self.race]["trait"].keys():
            for k, v in random.sample(traits.items(), k=4):
                rand_traits[k] = v
        else:
            rand_traits = deepcopy(races[self.race]["trait"])
            for k, v in random.sample(traits.items(), k=3):
                rand_traits[k] = v
        return rand_traits

    def get_mastered_weapon(self):
        if self.weapon_proficiency == "Light Melee":
            m_weapon = random.choice(light_weapons)
        elif self.weapon_proficiency == "Heavy Melee":
            m_weapon = random.choice(heavy_weapons)
        elif self.weapon_proficiency == "Ranged":
            m_weapon = random.choice(ranged_weapons)
        else:
            m_weapon = "Fists"
        return m_weapon

    def __init__(self):
        self.race = random.choice(list(races.keys()))
        self.hp = races[self.race]["hp"]
        self.traits = self.get_traits()
        if "Tough" in self.traits.keys():
            self.hp += 1
        self.weapon_proficiency = random.choice(weapon_proficiencies)
        self.mastered_weapon = self.get_mastered_weapon()
        self.equipment = deepcopy(adventurers_kit)
        self.money = "10 gp"

    def to_dict(self):
        return self.__dict__


if __name__ == "__main__":
    from pprint import pprint

    player_character = PlayerCharacter()
    pprint(player_character.to_dict())
