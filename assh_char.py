import dice
from utilities import mod_to_str
import random
import json
from copy import deepcopy
from assh_ability_adj import adjustments
from assh_class_data import class_info
from assh_spells import assh_magician_spells, assh_cleric_spells, dying_earth_spells


class PlayerCharacter:
    def _gen_abilities(self):
        abilities = {
            "STR": dice.roll_ndn_drop_n(4, 6, 1),
            "DEX": dice.roll_ndn_drop_n(4, 6, 1),
            "CON": dice.roll_ndn_drop_n(4, 6, 1),
            "INT": dice.roll_ndn_drop_n(4, 6, 1),
            "WIS": dice.roll_ndn_drop_n(4, 6, 1),
            "CHA": dice.roll_ndn_drop_n(4, 6, 1),
        }
        return abilities

    def _lookup_mods(self) -> dict:
        ability_mods = {}
        for a in self.abilities.keys():
            ability_mods[a] = deepcopy(adjustments[a][self.abilities[a]])
        return ability_mods

    def _get_stats_ranked(self):
        """
        docstring
        """
        stats_ranked = sorted(self.abilities, key=self.abilities.get, reverse=True)
        return stats_ranked

    def _determine_class(self):
        stat_map = {
            "STR": "Fighter",
            "DEX": "Thief",
            "INT": "Magician",
            "WIS": "Cleric",
        }
        for s in self.stats_ranked:
            if s in stat_map.keys():
                return stat_map[s]

    def _alignment(self):
        alignments = [
            "Neutral",
            "Lawful Good",
            "Chaotic Good",
            "Lawful Evil",
            "Chaotic Evil",
        ]
        weights = (50, 20, 20, 5, 5)
        if self.char_class in ["Fighter", "Magician", "Cleric"]:
            alignment = random.choices(alignments, weights=weights)[0]
        elif self.char_class == "Thief":
            weights = (50, 0, 30, 10, 10)
            alignment = random.choices(alignments, weights=weights)[0]
        else:
            alignment = None
        return alignment

    def _stringify_save_mods(self):
        for k, v in self.save_mods.items():
            self.save_mods[k] = mod_to_str(v)
        return

    def _stringify_ability_mods(self):
        mods_to_update = {
            "STR": [0, 1],
            "DEX": [0, 1],
            "CON": [0, 1],
            "WIS": [0],
            "CHA": [0, 2],
        }
        for x in mods_to_update.keys():
            for y in mods_to_update[x]:
                self.ability_mods[x][y] = mod_to_str(self.ability_mods[x][y])
        return

    def _weapon_atk_and_dmg(self):
        for i in range(len(self.char_info["Weapons"])):
            # add +1 to atk and damage for mastery
            if (
                self.char_class == "Fighter"
                and "Mastery" in self.char_info["Weapons"][i]["Other"]
            ):
                if self.char_info["Weapons"][i]["Range"] == "":
                    self.char_info["Weapons"][i]["Attack"] = mod_to_str(
                        self.melee_atk + 1
                    )
                    self.char_info["Weapons"][i]["Damage"] = (
                        f"{self.char_info['Weapons'][i]['Damage']}"
                        f"{mod_to_str(self.melee_dmg + 1)}"
                    )
                else:
                    self.char_info["Weapons"][i]["Attack"] = mod_to_str(
                        self.missile_atk + 1
                    )
                    self.char_info["Weapons"][i][
                        "Damage"
                    ] = f"{self.char_info['Weapons'][i]['Damage']}+1"
            else:
                if self.char_info["Weapons"][i]["Range"] == "":
                    self.char_info["Weapons"][i]["Attack"] = mod_to_str(self.melee_atk)
                    if self.melee_dmg != 0:
                        self.char_info["Weapons"][i]["Damage"] = (
                            f"{self.char_info['Weapons'][i]['Damage']}"
                            f"{mod_to_str(self.melee_dmg)}"
                        )
                elif "Dagger" in self.char_info["Weapons"][i]["Name"]:
                    self.char_info["Weapons"][i][
                        "Attack"
                    ] = f"{mod_to_str(self.melee_atk)}/{mod_to_str(self.missile_atk)}"
                    if self.melee_dmg != 0:
                        self.char_info["Weapons"][i]["Damage"] = (
                            f"{self.char_info['Weapons'][i]['Damage']}"
                            f"{mod_to_str(self.melee_dmg)}"
                        )
                elif "Sling" in self.char_info["Weapons"][i]["Name"]:
                    self.char_info["Weapons"][i]["Attack"] = mod_to_str(
                        self.missile_atk
                    )
                    if self.melee_dmg != 0:
                        self.char_info["Weapons"][i]["Damage"] = (
                            f"{self.char_info['Weapons'][i]['Damage']}"
                            f"{mod_to_str(self.melee_dmg)}"
                        )
                else:
                    self.char_info["Weapons"][i]["Attack"] = mod_to_str(
                        self.missile_atk
                    )

    def _spell_list(self):
        spell_list = []
        if self.char_class == "Cleric":
            if self.cleric_spell_src == "assh_cleric_spells":
                spell_list = random.sample(assh_cleric_spells[1], k=3)
            else:
                pass
        elif self.char_class == "Magician":
            if self.magician_spell_src == "assh_magician_spells":
                spell_list = random.sample(assh_magician_spells[1], k=3)
            elif self.magician_spell_src == "dying_earth":
                spell_list.append(
                    random.choice(dying_earth_spells["Offensive"])["name"]
                )
                spell_list.append(
                    random.choice(dying_earth_spells["Defensive"])["name"]
                )
                spell_list.append(
                    random.choice(dying_earth_spells["Miscellaneous"])["name"]
                )
            else:
                pass
        else:
            pass
        spell_list.sort()
        return spell_list

    def _update_thief_abilities(self):
        if self.abilities["DEX"] >= 16:
            self.char_info["Class Abilities"]["Thief Abilities"]["Climb"] += 1
            self.char_info["Class Abilities"]["Thief Abilities"]["Hide"] += 1
            self.char_info["Class Abilities"]["Thief Abilities"][
                "Manipulate Traps"
            ] += 1
            self.char_info["Class Abilities"]["Thief Abilities"]["Move Silently"] += 1
            self.char_info["Class Abilities"]["Thief Abilities"]["Open Locks"] += 1
            self.char_info["Class Abilities"]["Thief Abilities"]["Pick Pockets"] += 1
        if self.abilities["INT"] >= 16:
            self.char_info["Class Abilities"]["Thief Abilities"]["Decipher Script"] += 1
            # Cannot read scrolls until level 5
            # self.char_info['Class Abilities']['Thief Abilities']['Read Scrolls'] += 1
        if self.abilities["WIS"] >= 16:
            self.char_info["Class Abilities"]["Thief Abilities"]["Discern Noise"] += 1
        return

    def _format_thief_abilities(self):
        for k, v in self.char_info["Class Abilities"]["Thief Abilities"].items():
            self.char_info["Class Abilities"]["Thief Abilities"][k] = (
                f"{v}:12" if v != "-" else v
            )
        return

    def __init__(
        self,
        class_choice="random",
        cleric_spell_src="assh_cleric_spells",
        magician_spell_src="assh_magician_spells",
    ):
        self.class_choice = class_choice
        self.cleric_spell_src = cleric_spell_src
        self.magician_spell_src = magician_spell_src

        self.abilities = self._gen_abilities()
        self.ability_mods = self._lookup_mods()
        self.stats_ranked = self._get_stats_ranked()
        self.best_stat = self.stats_ranked[0]
        self.char_class = self._determine_class()
        self.alignment = self._alignment()
        self.char_info = deepcopy(class_info[self.char_class])
        self.hp = self.char_info["HD"] + self.ability_mods["CON"][0]
        self.fa = self.char_info["FA"]
        self.fighting_ability = mod_to_str(self.fa)
        self.armor = self.char_info["Armor"]["Type"]
        self.ac = self.char_info["Armor"]["AC"] + self.ability_mods["DEX"][1]
        self.dr = self.char_info["Armor"]["DR"]
        self.mv = self.char_info["Armor"]["MV"]
        self.melee_atk = self.fa + self.ability_mods["STR"][0]
        self.missile_atk = self.fa + self.ability_mods["DEX"][0]
        self.melee_dmg = self.ability_mods["STR"][1]
        self._weapon_atk_and_dmg()
        self._stringify_ability_mods()
        self.base_save = 16
        self.save_mods = self.char_info["Saving Throws"]
        self._stringify_save_mods()
        self.spell_list = self._spell_list()
        if self.char_class == "Thief":
            self._update_thief_abilities()
            self._format_thief_abilities()

    def to_dict(self):
        char_dict = self.__dict__
        return char_dict

    def to_json(self):
        char_json = json.dumps(self.__dict__)
        return char_json


if __name__ == "__main__":
    from pprint import pprint

    my_pc = PlayerCharacter()
    pprint(my_pc.to_dict())
