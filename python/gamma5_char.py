import random
import dice
from copy import deepcopy
from math import floor
from gamma5_data import bio, mutations


class PlayerCharacter:
    def _bio(self):
        return random.choice(list(bio.keys()))

    def _ability_scores(self):

        abilities = {}

        for ability, how in bio[self.bio]["abilities"].items():
            if how in ["16", "18"]:
                score = int(how)
            elif how == "3d6":
                score = dice.roll_dice(3, 6)
            elif how == "3d6+2":
                score = dice.roll_dice(3, 6) + 2
            elif how == "3d6+3":
                score = dice.roll_dice(3, 6) + 3
            else:
                score = 0
            abilities[ability] = score

        return abilities

    def _save_profs(self, save_index):
        if save_index == 1:
            return random.choice(["DEX", "CON", "WIS"])
        elif save_index == 2:
            return random.choice(["STR", "INT", "CHA"])
        else:
            raise ValueError("Invalid value for save_index, must be 1 or 2")

    def _mutations(self):
        char_mutations = deepcopy(bio[self.bio]["bio_mutations"])
        k = bio[self.bio]["random_mutations"]
        char_mutations.extend(random.sample(list(mutations.keys()), k=k))
        return char_mutations

    def _mod_calc(self, score: int) -> int:
        mod = floor((score - 10) / 2)
        return mod

    def _ability_mods(self):
        ability_mods = {}
        for ability in self.abilities.keys():
            ability_mods[ability] = self._mod_calc(self.abilities[ability])
        return ability_mods

    def __init__(self):
        self.bio = self._bio()
        self.bio_info = bio[self.bio]
        self.abilities = self._ability_scores()
        self.prof_bonus = 2
        self.save_prof1 = self._save_profs(1)
        self.save_prof2 = self._save_profs(2)
        self.size = self.bio_info["size"]
        self.speed1 = self.bio_info["speed1"]
        self.speed2 = self.bio_info["speed2"]
        self.speed2_type = self.bio_info["speed2_type"]
        self.mutations = self._mutations()
        self.ability_mods = self._ability_mods()

        # placeholder for calculating saving throw mods
        # self.hp = 12 + CON mod

    def to_dict(self):
        return self.__dict__


if __name__ == "__main__":
    from pprint import pprint

    pc = PlayerCharacter()
    pprint(pc.to_dict())
