import random
from typing import Dict, List

from rpg_tools.misc_data.dcc_occupations import OCCUPATIONS
from rpg_tools.misc_data.knave_spells import SPELLS
from rpg_tools.utils.dice import roll_dice

skills = [
    {
        "Dungeoneering": (
            "Navigate dungeons and caves, detect grades and slopes, "
            "identify subterranean creatures."
        ),
    },
    {
        "Fast-Talk": "Convince another through charisma or subterfuge.",
    },
    {
        "Hypermnesia": "Perfectly recall information the character was previously exposed to.",
    },
    {
        "Intuition": "Discern lies or malicious intent; notice an important detail.",
    },
    {
        "Knowledge": (
            "Awareness of a bit of lore, science, or trivia that may be relevant to the situation."
        ),
    },
    {
        "Legerdemain": "Performing card tricks, picking pockets, and similar.",
    },
    {
        "Muscle": "Break down doors, lift heavy things, etc.",
    },
    {
        "Parkour": "Balancing, climbing, jumping, tumbling.",
    },
    {
        "Sneak": "Quietly move or hide without being noticed.",
    },
    {
        "Survival": (
            "Navigate, find food and shelter, track animals and people while in the wilderness."
        ),
    },
    {
        "Tinkering": (
            "Pick locks, set or disarm traps, discern how technological items work. "
            "Tools may be required."
        ),
    },
    {
        "Zoophilism": "Ability to calm, empathize with, and communicate in a "
        "rudimentary fashion with animals."
    },
]
extraordinary_abilities = [
    {
        "Alchemy": (
            "Mix potions and poisons, provided the necessary ingredients are at hand. "
            "Identify unknown liquids with a successful check."
        ),
    },
    {
        "Beastmaster": (
            "Make a check to tame a beast who's hit points don't exceed your own. "
            "The pet must be fed and treated well. If ever neglected, or called on to "
            "aid in direct combat, another check must be made to prevent the creature from "
            "abandoning you. If this ability is taken a second time, or you have the "
            "zoophilism skill, the checks are successful on 4+."
        ),
    },
    {
        "Berserks Mode": (
            "You may choose to enter a berserker rage, which lasts until the end of a "
            "combat. All attacks are made with disadvantage, but deal double damage on a hit."
        ),
    },
    {
        "Cantraps": "Produce minor, non-damaging magical effects at will.",
    },
    {
        "Diehard": (
            "The first time you fall to 0 hit points in a given day, you immediately gain "
            "1 hit point back and don't lose consciousness."
        ),
    },
    {
        "Healing": (
            "As an action, you can make a check to heal an ally other than yourself. "
            "On a success, the target creature is healed for 2 hit points. Alternatively, "
            "this ability can also be used to cure poison, disease, and other physical "
            "ailments that are non-magical. You must touch the recipient to perform the healing."
        ),
    },
    {
        "Read Magic": (
            "Ability to discern arcane writing and cast spells from scrolls. When this ability "
            "is gained, the character also gains two randomly determined scrolls (see Magic)."
        ),
    },
    {
        "Repel Undead": (
            "On a successful check, you add the total of the two dice and turn away that many "
            "hit points of undead creatures. May be attempted once per combat."
        ),
    },
    {
        "Vigilant": (
            "Whenever your side loses initiative, make a check. If the check is successful, "
            "you act first."
        ),
    },
    {
        "Wizardry": (
            "Knowledge of and ability to cast three randomly determined spells (see Magic). "
            "This ability may be taken multiple times, and three additional random spells "
            "are learned each time."
        ),
    },
    {
        "Perceptive": (
            "You have a chance to notice secret doors or other important yet subtle clues "
            "that others would miss. The GM needs to make the checks for this, and may need "
            "to be reminded from time to time that you have this ability."
        ),
    },
    {
        "Weapon Training": "You make combat checks with skill for a specific weapon group.",
    },
]

base_equipment = [
    "Rucksack",
    "Rations (7)",
    "Waterskin",
    "Flint & Steel",
    "Torches (6)",
]
clothing_items = [
    "Helmet",
    "Fine Cape",
    "Stylish Hat",
    "Hooded Woolen Cloak",
    "Eye Patch",
    "Bandit Mask",
]
equipment_a = [
    "Lasso",
    "Flask of Acid",
    "Pouch of Marbles",
    "Ball of Twine (100')",
    "Flask of Oil (2)",
    "Molotov Cocktail",
]
equipment_b = [
    "Prybar",
    "Whistle",
    "Skeleton Key",
    "Hammer, 10 Pitons",
    "Spyglass",
    "Lock Picks",
]
equipment_c = [
    "10' Pole",
    "Pouch of Sand",
    "Compass",
    "Jar of Lard",
    "Pliers",
    "Rope (50')",
]
light_melee_weapons = [
    "Dagger",
    "Stiletto",
    "Hand Axe",
    "Mace",
    "Nunchaku",
    "Sword",
    "Quarterstaff",
]
heavy_melee_weapons = [
    "Battle Axe",
    "Double-Bladed Scimitar",
    "Bat'leth",
    "Greatclub",
    "Glaive",
    "Halberd",
    "Polearm",
    "Maul",
    "Zweihänder",
]
ranged_weapons = [
    "Crossbow, Boltcase of 12 Bolts",
    "Bow, Quiver of 12 Arrows",
    "Darts, Bandolier of 12",
    "Javelins, Sheaf of 6",
    "Shuriken, Bandolier of 12",
    "Sling, Pouch of 12 Stones",
]


class D666Character:
    """Yeah."""

    def __init__(self, level: int = 1) -> None:
        self.name: str = ""
        self.level: int = level
        self.hit_points: int = 3
        self.skills_count: int = 2
        self.extraordinary_abilities_count: int = 1
        self.level_abilities()
        self.skills: List[Dict[str, str]] = self.get_skills()
        self.extraordinary_abilities: List[
            Dict[str, str]
        ] = self.get_extraordinary_abilities()
        self.special_ea_rules()
        self.weapon: str = self.get_weapon()
        self.equipment: List[str] = self.get_equipment()
        self.background: str = self.get_background()
        self.spells: List[Dict[str, str]] = self.get_spells()
        self.money: str = f"{roll_dice(3, 6)} sp"

    def level_abilities(self):
        for _ in range(self.level - 1):
            roll = roll_dice(1, 6)
            if 1 <= roll <= 3:
                self.hit_points += 1
            elif 4 <= roll <= 5:
                self.skills_count += 1
            elif roll == 6:
                self.extraordinary_abilities_count += 1
            else:
                raise Exception(f"Invalid roll ({roll}) not between 1 and 6.")

    def get_skills(self):
        _skills = random.sample(skills, k=self.skills_count)
        return _skills

    def get_extraordinary_abilities(self):
        _extraordinary_abilities = random.sample(
            extraordinary_abilities,
            k=self.extraordinary_abilities_count,
        )
        return _extraordinary_abilities

    def special_ea_rules(self):
        """Check for special rules."""
        ea_keys = [list(ea.keys())[0] for ea in self.extraordinary_abilities]
        self.has_wizardry = "Wizardry" in ea_keys
        self.has_weapon_training = "Weapon Training" in ea_keys
        self.check_for_weapon_training()
        self.get_spells()

    def check_for_weapon_training(self):
        """Check if character has the 'Weapon Training' extraordinary ability."""
        self.trained_weapon = None
        if self.has_weapon_training:
            self.trained_weapon = random.choice(
                [
                    "Unarmed",
                    "Light Melee",
                    "Heavy Melee",
                    "Ranged",
                ]
            )
        for ea in self.extraordinary_abilities:
            if list(ea.keys())[0] == "Weapon Training":
                ea[
                    "Weapon Training"
                ] = f"You make {self.trained_weapon} combat checks as skilled."

    def get_weapon(self):
        if self.has_weapon_training:
            if self.trained_weapon == "Light Melee":
                weapon = random.choice(light_melee_weapons)
            elif self.trained_weapon == "Heavy Melee":
                weapon = random.choice(heavy_melee_weapons)
            elif self.trained_weapon == "Ranged":
                weapon = random.choice(ranged_weapons)
            elif self.trained_weapon == "Unarmed":
                weapon = "Unarmed"
        else:
            weapon = random.choice(
                light_melee_weapons + heavy_melee_weapons + ranged_weapons
            )
        return weapon

    def get_equipment(self):
        """Base equipment plus one item from each list."""
        equipment = []
        equipment.extend(base_equipment)
        for items in [
            clothing_items,
            equipment_a,
            equipment_b,
            equipment_c,
        ]:
            equipment.append(random.choice(items))
        return equipment

    def get_background(self):
        """Roll on the DCC occupations table."""
        roll = roll_dice(1, 100)
        single_occ = [x for x in OCCUPATIONS if "-" not in x[0]]
        range_occ = [x for x in OCCUPATIONS if "-" in x[0]]
        result = [x for x in single_occ if int(x[0]) == roll]
        if len(result) == 0:
            result = [
                x
                for x in range_occ
                if int(x[0].split("-")[0]) <= roll <= int(x[0].split("-")[1])
            ]
        assert len(result) == 1
        background = (
            result[0][1]
            .replace("Dwarven ", "")
            .replace("Elven ", "")
            .replace("Halfling ", "")
            .title()
        )
        self.equipment.append(result[0][3])
        return background

    def get_spells(self):
        """Roll on the Knave spells table if character has Wizardry."""
        spells = []
        if self.has_wizardry:
            spell_keys = random.sample(list(SPELLS.keys()), k=3)
            print(f"{spell_keys = }")
            spells = [{k: v} for k, v in SPELLS.items() if k in spell_keys]
        return spells


if __name__ == "__main__":
    from pprint import pprint

    level = roll_dice(1, 9)
    print(f"{level = }")
    character = D666Character(level=level)
    pprint(character.__dict__)
