import random
import dice
from copy import deepcopy
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

    def _mutations(self):
        char_mutations = deepcopy(bio[self.bio]["bio_mutations"])
        k = bio[self.bio]["random_mutations"]
        char_mutations.extend(random.sample(list(mutations.keys()), k=k))
        return char_mutations

    def _ability_mod(self, ability: str) -> int:
        # score
        # mod =
        # return mod
        pass

    def __init__(self):
        self.bio = self._bio()
        self.bio_info = bio[self.bio]
        self.abilities = self._ability_scores()
        self.size = self.bio_info["size"]
        self.speed1 = self.bio_info["speed1"]
        self.speed2 = self.bio_info["speed2"]
        self.speed2_type = self.bio_info["speed2_type"]
        self.mutations = self._mutations()

        # self.STR_mod = self._ability_mods()

        # self.hp =

    def to_dict(self):
        return self.__dict__


if __name__ == "__main__":
    from pprint import pprint

    pc = PlayerCharacter()
    pprint(pc.to_dict())
