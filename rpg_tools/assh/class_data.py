class_info = {
    "Fighter": {
        "HD": 10,
        "FA": 1,
        "Saving Throws": {
            "Death": 2,
            "Transformation": 2,
            "Device": 0,
            "Avoidance": 0,
            "Sorcery": 0,
        },
        "Class Abilities": {
            "Heroic Fighting": (
                "When fighting creatures of 1 HD or less, double number of attacks "
                "per round"
            ),
            "Weapon Mastery (2)": (
                "+1 to attack and damage rolls, increased attack rate"
            ),
        },
        "Alignment": "Any",
        "Armor Allowed": "Any",
        "Shields Allowed": "Any",
        "Favored Weapons": "Any",
        "Weapons": [
            {
                "Name": "Battle Axe",
                "WC": 2,
                "Attack Rate": "3/2",
                "Damage": "1d8",
                "Range": "",
                "Other": "Mastery, Versatile (1d10)",
            },
            {
                "Name": "Short Bow",
                "WC": None,
                "Attack Rate": "3/2",
                "Damage": "1d6",
                "Range": "50/100/150",
                "Other": "Mastery",
            },
        ],
        "Armor": {
            "Type": "Scale Armor",
            "AC": 13,
            "DR": 1,
            "MV": 30,
            "Weight Class": "Medium",
        },
        "Equipment": [
            "backpack",
            "bandages",
            "large sack",
            "soft leather pouch",
            "quiver of arrows (12)",
            "hemp rope",
            "tinderbox",
            "torches (2)",
            "wineskin (full)",
            "iron rations (7)",
        ],
        "XP Next": 2000,
    },
    "Thief": {
        "HD": 6,
        "FA": 1,
        "Saving Throws": {
            "Death": 0,
            "Transformation": 0,
            "Device": 2,
            "Avoidance": 2,
            "Sorcery": 0,
        },
        "Class Abilities": {
            "Agile": (
                "+1 AC bonus when unarmored and unemcumbered (small shield allowed)"
            ),
            "Backstab": (
                "An attack from behind with a class 1 or 2 melee weapon with which "
                "the thief is skilled. The target must be unaware of the attack. The "
                "attack roll is made at a +4 bonus. Double weapon damage dice are "
                "rolled."
            ),
            "Clandestine Tongue": "Thieves' Cant",
            "Detect Secret Doors": "Base 3:6 chance",
            "Thief Abilities": {
                # chance in 12
                "Climb": 8,
                "Decipher Script": 0,
                "Discern Noise": 4,
                "Hide": 5,
                "Manipulate Traps": 3,
                "Move Silently": 5,
                "Open Locks": 3,
                "Pick Pockets": 4,
                "Read Scrolls": "-",
            },
        },
        "Alignment": "Any, save Lawful Good",
        "Armor Allowed": "Light",
        "Shields Allowed": "Small",
        "Favored Weapons": (
            "Axe (hand), Bow (short), Club (light), Crossbow (light), Dagger, Dart, "
            "Flail (horseman’s), Garrotte, Hammer (horseman’s), Mace (horseman’s), "
            "Pick (horseman’s), Sling, Sword (short, falcata, long, broad)"
        ),
        "Weapons": [
            {
                "Name": "Short Sword",
                "WC": 1,
                "Attack Rate": "1/1",
                "Damage": "1d6",
                "Range": "",
                "Other": "",
            },
            {
                "Name": "Darts (x2)",
                "WC": None,
                "Attack Rate": "1/1",
                "Damage": "1d3",
                "Range": "15/30/45",
                "Other": "",
            },
        ],
        "Armor": {
            "Type": "Leather Armor",
            "AC": 12,
            "DR": 0,
            "MV": 40,
            "Weight Class": "Light",
        },
        "Equipment": [
            "backpack",
            "bandages",
            "large sack",
            "soft leather pouch",
            "chalk",
            "dice",
            "fishing hooks (12)",
            "fishing string",
            "grappling hook",
            "silk rope",
            "spool of wire",
            "writing stick",
            "thieves tools",
            "tinderbox",
            "torches (2)",
            "iron rations (7)",
        ],
        "XP Next": 1500,
    },
    "Magician": {
        "HD": 4,
        "FA": 0,
        "Saving Throws": {
            "Death": 0,
            "Transformation": 0,
            "Device": 2,
            "Avoidance": 0,
            "Sorcery": 2,
        },
        "Class Abilities": {
            "Magician's Familiar": (
                "To summon a smnall animal of 1d3+1 hp to function as a familiar"
            ),
            "Read Magic": (
                "The ability to decipher otherwise unintelligible magical "
                "inscriptions or symbols placed on weapons, armour, items, doors, "
                "walls, and other media by means of the sorcerer mark spell or other "
                "like methods"
            ),
            "Read Scrolls": "To decipher and invoke spells on magician scrolls",
            "Scribe Scrolls": (
                "To write from one to five known spells onto a scroll, creating a "
                "single-use magical device, at a cost of 500 gp + 100 gp per spell "
                "level"
            ),
        },
        "Alignment": "Any",
        "Armor Allowed": "None",
        "Shields Allowed": "None",
        "Favored Weapons": "Dagger, Dart, Quarterstaff, Sling",
        "Weapons": [
            {
                "Name": "Silver Dagger",
                "WC": 1,
                "Attack Rate": "1/1",
                "Damage": "1d4",
                "Range": "10/20/30",
                "Other": "",
            },
            {
                "Name": "Quarterstaff",
                "WC": 3,
                "Attack Rate": "1/1",
                "Damage": "1d6",
                "Range": "",
                "Other": "",
            },
            {
                "Name": "Sling",
                "WC": None,
                "Attack Rate": "1/1",
                "Damage": "1d4",
                "Range": "50/100/150",
                "Other": "",
            },
        ],
        "Armor": {
            "Type": "None",
            "AC": 10,
            "DR": 0,
            "MV": 40,
            "Weight Class": "-",
        },
        "Equipment": [
            "backpack",
            "small sack",
            "soft leather pouch",
            "bandages",
            "sling bullets (20)",
            "blanket",
            "chalk",
            "ink and quill",
            "incendiary oil",
            "parchment (2)",
            "silk rope",
            "writing stick",
            "tinderbox",
            "torches (3)",
            "wineskin (full)",
            "standard rations (7)",
            "spell book",
        ],
        "XP Next": 2500,
    },
    "Cleric": {
        "HD": 8,
        "FA": 1,
        "Saving Throws": {
            "Death": 2,
            "Transformation": 0,
            "Device": 0,
            "Avoidance": 0,
            "Sorcery": 2,
        },
        "Class Abilities": {
            "Read Scrolls": "To decipher and invoke spells on cleric scrolls",
            "Scribe Scrolls": (
                "To write from one to five known spells onto a scroll, creating a "
                "single-use magical device, at a cost of 500 gp + 100 gp per spell "
                "level"
            ),
            "Turn Undead": (
                "All clerics can exert control over the undead and some dæmonic "
                "beings, causing them to flee and/or cower. This ability can be used "
                "a number of times per day equal to the character's level; however, "
                "the cleric can make but one attempt per encounter."
            ),
        },
        "Alignment": "Any",
        "Armor Allowed": "Any",
        "Shields Allowed": "Any",
        "Favored Weapons": (
            "Club (light, war), Dagger, Flail (horseman’s, footman’s), Hammer "
            "(horseman’s, war), Lasso, Mace (horseman’s, footman’s), Morning Star, "
            "Quarterstaff, Spear (short, long), Spiked Staff, Sword (short, long, "
            "broad, bastard), Whip"
        ),
        "Weapons": [
            {
                "Name": "War Hammer",
                "WC": 2,
                "Attack Rate": "1/1",
                "Damage": "1d8",
                "Range": "",
                "Other": "Versatile (1d10)",
            },
            {
                "Name": "Dagger",
                "WC": 1,
                "Attack Rate": "1/1",
                "Damage": "1d4",
                "Range": "10/20/30",
                "Other": "",
            },
        ],
        "Armor": {
            "Type": "Studded Armor",
            "AC": 13,
            "DR": 0,
            "MV": 40,
            "Weight Class": "Light",
        },
        "Equipment": [
            "backpack",
            "bandages",
            "soft leather pouch",
            "small sack",
            "tinderbox",
            "torches (3)",
            "wineskin (full)",
            "writing stick",
            "iron rations (7)",
            "holy water",
            "silver holy symbol",
        ],
        "XP Next": 2000,
    },
}
