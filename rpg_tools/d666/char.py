import random
from typing import Dict, List

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
    # TODO: Add one more
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
    # TODO: Add another item
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
    "Zweihander",
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
        self.weapon: str = self.get_weapon()
        self.equipment: List[str] = self.get_equipment()

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

    def get_weapon(self):
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


if __name__ == "__main__":
    from pprint import pprint

    level = roll_dice(1, 9)
    print(f"{level = }")
    character = D666Character(level=level)
    pprint(character.__dict__)
