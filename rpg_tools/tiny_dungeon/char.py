from copy import deepcopy
import random
from typing import Optional

from rpg_tools.tiny_dungeon.data import (
    races,
    traits,
    adventurers_kit,
    weapon_proficiencies,
    light_weapons,
    heavy_weapons,
    ranged_weapons,
)


class PlayerCharacter:
    def __init__(self, race: Optional[str] = None):
        if race:
            race = race.capitalize()
            if race in races:
                self.race = race
            else:
                self.race = random.choice(list(races.keys()))
        else:
            self.race = random.choice(list(races.keys()))
        self.hp = races[self.race]["hp"]
        self.racial_trait = races[self.race].get("trait")
        self.traits = self.get_traits()
        if "Tough" in [x["name"] for x in self.traits]:
            self.hp += 1
        self.weapon_proficiency = random.choice(weapon_proficiencies)
        self.mastered_weapon = self.get_mastered_weapon()
        self.equipment = deepcopy(adventurers_kit)
        self.money = "10 gp"

    def get_traits(self):
        num_traits = 3
        if self.race == "Human":
            num_traits += 1
        rand_traits = random.sample(traits, k=num_traits)
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

    def to_dict(self):
        return self.__dict__


if __name__ == "__main__":
    from pprint import pprint

    player_character = PlayerCharacter()
    pprint(player_character.to_dict())
