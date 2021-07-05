import random
import dice
from copy import deepcopy
from math import floor
from gamma5_data import bio, mutations, random_skills, skills


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
        # TODO: Subroutine to select from bite/horns/talons for beast
        char_mutations = deepcopy(bio[self.bio]["bio_mutations"])
        if "Bite/Horns/Talons" in char_mutations:
            # TODO: Maybe DEX can get better later from mutation and ruin this?
            if self.abilities["DEX"] > self.abilities["STR"]:
                attack = "Talons"
            else:
                attack = random.choice(["Bite", "Horns"])
            char_mutations.append(attack)
            char_mutations.remove("Bite/Horns/Talons")
        random_mutations = bio[self.bio]["random_mutations"]
        for i in range(random_mutations):
            char_mutations.append(
                random.choice([x for x in mutations.keys() if x not in char_mutations])
            )
        return char_mutations

    def _apply_mutations(self):
        for m in self.mutations:
            if m == "Bite":
                self.weapons.append(
                    {
                        "Name": "Bite",
                        "Ability": "STR",
                        "Damage": "1d10",
                        "Type": "P",
                        "Range": "Melee",
                    }
                )
            elif m == "Climber":
                self.speed["Climb"] = 30
            elif m == "Formidable Charisma":
                self.abilities["CHA"] += 4
            elif m == "Formidable Constitution":
                self.abilities["CON"] += 4
            elif m == "Formidable Dexterity":
                self.abilities["DEX"] += 4
            elif m == "Formidable Intelligence":
                self.abilities["INT"] += 4
            elif m == "Formidable Strength":
                self.abilities["STR"] += 4
            elif m == "Formidable Wisdom":
                self.abilities["WIS"] += 4
            elif m == "Gamma Eyes":
                self.weapons.append(
                    {
                        "Name": "Gamma Eyes",
                        "Ability": "DEX",
                        "Damage": "2d6",
                        "Type": "Radiation",
                        "Range": "30'",
                    }
                )
            elif m == "Gauss Spike":
                self.weapons.append(
                    {
                        "Name": "Gauss Spike",
                        "Ability": "DEX",
                        "Damage": "2d4 + Prone",
                        "Type": "Force",
                        "Range": "30'",
                    }
                )
            elif m == "Greater Saving Throw":
                save_options = [
                    x for x in ["DEX", "CON", "INT"] if x not in self.save_profs
                ]
                self.save_profs.append(random.choice(save_options))
            elif m == "Horns":
                self.weapons.append(
                    {
                        "Name": "Horns",
                        "Ability": "STR",
                        "Damage": "2d6",
                        "Type": "P",
                        "Range": "Melee",
                    }
                )
            elif m == "Quick":
                for k in self.speed.keys():
                    self.speed[k] += 10
            elif m == "Talons":
                self.weapons.append(
                    {
                        "Name": "Talons",
                        "Ability": "DEX",
                        "Damage": "1d6",
                        "Type": "S",
                        "Range": "Melee",
                    }
                )
            elif m == "Thick Hide":
                self.armor_items.append(
                    {
                        "Name": "Thick Hide",
                        "AC Bonus": 2,
                        "Max Dex Bonus": None,
                    }
                )
            elif m == "Toughened":
                self.hd += 1
            elif m == "Wings":
                fly_speed = self.speed["Walk"]
                self.speed["Fly"] = fly_speed
        return

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

    def _hit_points(self):
        hp = 12 + self.abilities["CON"]
        for i in range(self.hd - 1):
            hp += 7 + self.abilities["CON"]
        return hp

    def _skills(self):
        skills = []
        # add bio skills
        bio_skills = self.bio_info["skills"]
        skills.extend([x for x in bio_skills if x != "random"])
        if "random" in bio_skills:
            skills.append(random.choice([x for x in random_skills if x not in skills]))
        # everyone gets 4 additional random skills
        for i in range(4):
            skills.append(random.choice([x for x in random_skills if x not in skills]))
        return skills

    def _skill_mods(self):
        skill_mods = {}
        for skill, ability in skills.items():
            if skill in self.skill_profs:
                skill_mods[skill] = self.ability_mods[ability] + self.prof_bonus
            else:
                skill_mods[skill] = self.ability_mods[ability]
        return skill_mods

    def __init__(self):
        self.level = 1
        self.hd = 1
        self.hd_type = "d12"
        self.bio = self._bio()
        self.bio_info = bio[self.bio]
        self.abilities = self._ability_scores()
        self.prof_bonus = 2
        self.save_profs = self._save_profs()
        self.size = self.bio_info["size"]
        self.speed = self.bio_info["speed"]
        self.weapons = []
        self.armor_items = []
        self.mutations = self._mutations()
        self._apply_mutations()
        self.ability_mods = self._ability_mods()
        self.save_mods = self._save_mods()
        self.hp = self._hit_points()
        self.skill_profs = self._skills()
        self.skill_mods = self._skill_mods()
        self.ac = 10 + self.abilities["DEX"]
        self.initiative = self.abilities["DEX"]

    def to_dict(self):
        return self.__dict__


if __name__ == "__main__":
    from pprint import pprint

    pc = PlayerCharacter()
    pprint(pc.to_dict())
