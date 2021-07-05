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

    def _save_profs(self):
        save_profs = [
            random.choice(["DEX", "CON", "WIS"]),
            random.choice(["STR", "INT", "CHA"]),
        ]
        return save_profs

    def _mutations(self):
        # TODO: Ensure random mutations aren't repeats of bio mutations
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

    def _save_mods(self):
        save_mods = {}
        for ability in bio[self.bio]["abilities"].keys():
            if ability in self.save_profs:
                save_mods[ability] = self.ability_mods[ability] + self.prof_bonus
            else:
                save_mods[ability] = self.ability_mods[ability]
        return save_mods

    def __init__(self):
        self.bio = self._bio()
        self.bio_info = bio[self.bio]
        self.abilities = self._ability_scores()
        self.prof_bonus = 2
        self.save_profs = self._save_profs()
        self.size = self.bio_info["size"]
        self.speed = self.bio_info["speed"]
        self.mutations = self._mutations()
        self.ability_mods = self._ability_mods()
        self.save_mods = self._save_mods()

        # placeholder for calculating saving throw mods
        # self.hp = 12 + CON mod

    def to_dict(self):
        return self.__dict__


if __name__ == "__main__":
    from pprint import pprint

    pc = PlayerCharacter()
    pprint(pc.to_dict())
