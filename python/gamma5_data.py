import random
from dice import roll_dice

bio = {
    "Avian": {
        "abilities": {
            "STR": "3d6",
            "DEX": "16",
            "CON": "3d6",
            "INT": "3d6",
            "WIS": "16",
            "CHA": "3d6",
        },
        "size": "Medium",
        "speed": {
            "Walk": 30,
            "Fly": 30,
        },
        "skills": [
            "Perception",
        ],
        "features": [],
        "bio_mutations": [
            "Low-Light Vision",
            "Talons",
            "Wings",
        ],
        "random_mutations": 3,
    },
    "Beast": {
        "abilities": {
            "STR": "16",
            "DEX": "3d6",
            "CON": "16",
            "INT": "3d6",
            "WIS": "3d6",
            "CHA": "3d6",
        },
        "size": "Medium",
        "speed": {
            "Walk": 40,
        },
        "skills": [
            "Stealth",
        ],
        "features": [],
        "bio_mutations": [
            "Darkvision",
            "Bite/Horns/Talons",
        ],
        "random_mutations": 3,
    },
    "Bug": {
        "abilities": {
            "STR": "3d6",
            "DEX": "3d6",
            "CON": "18",
            "INT": "3d6",
            "WIS": "3d6",
            "CHA": "3d6",
        },
        "size": "Medium",
        "speed": {
            "Walk": 30,
            "Climb": 30,
        },
        "skills": [
            "Survival",
        ],
        "features": [],
        "bio_mutations": [
            "Blindsight",
            "Climber",
            "Radiation Resistance",
            "Thick Hide",
        ],
        "random_mutations": 3,
    },
    "Mutated Human": {
        "abilities": {
            "STR": "3d6+2",
            "DEX": "3d6+2",
            "CON": "3d6+2",
            "INT": "3d6+2",
            "WIS": "3d6+2",
            "CHA": "3d6+2",
        },
        "size": "Medium",
        "speed": {
            "Walk": 30,
        },
        "skills": [
            "random",
        ],
        "features": [],
        "bio_mutations": [],
        "random_mutations": 5,
    },
    "Pure Strain Human": {
        "abilities": {
            "STR": "3d6+3",
            "DEX": "3d6+3",
            "CON": "3d6+3",
            "INT": "3d6+3",
            "WIS": "3d6+3",
            "CHA": "3d6+3",
        },
        "size": "Medium",
        "speed": {
            "Walk": 30,
        },
        "skills": [
            "Ancient Tech",
            "random",
        ],
        "features": [],
        "bio_mutations": [],
        "random_mutations": 0,
    },
    "Plant": {
        "abilities": {
            "STR": "3d6",
            "DEX": "3d6",
            "CON": "18",
            "INT": "3d6",
            "WIS": "3d6",
            "CHA": "3d6",
        },
        "size": "Medium",
        "speed": {
            "Walk": 25,
        },
        "skills": [
            "Nature",
        ],
        "features": [("Flammable", "Vulnerable to fire damage")],
        "bio_mutations": [
            "Blindsight",
            "Poison Resistance",
            "Radiation Resistance",
            "Rooted",
        ],
        "random_mutations": 3,
    },
    "Robot": {
        "abilities": {
            "STR": "16",
            "DEX": "3d6",
            "CON": "3d6",
            "INT": "16",
            "WIS": "3d6",
            "CHA": "3d6",
        },
        "size": "Medium",
        "speed": {
            "Walk": 30,
        },
        "skills": [
            "Investigation",
        ],
        "features": [
            (
                "Tin Man",
                (
                    "You're not considered a living creature, and do not need to eat, "
                    "drink, breathe or sleep. You can eat or drink if you want. In "
                    "addition, you are immune to radiation, poison and poison damage, "
                    "disease, and petrification. You cannot be put to sleep. You do, "
                    "however, take short and long rests (cooling down your systems), "
                    "are unconscious when at 0 hp (you can be stabilized with a DC 10 "
                    "Intelligence (Science) check); you are destroyed (which means "
                    "your character 'dies') if you fail three death saves or take "
                    "massive damage."
                ),
            )
        ],
        "bio_mutations": [
            "Darkvision",
        ],
        "random_mutations": 3,
    },
    "Saurian": {
        "abilities": {
            "STR": "16",
            "DEX": "3d6",
            "CON": "16",
            "INT": "3d6",
            "WIS": "3d6",
            "CHA": "3d6",
        },
        "size": "Medium",
        "speed": {
            "Walk": 30,
        },
        "skills": [
            "Intimidation",
        ],
        "features": [],
        "bio_mutations": [
            "Darkvision",
            "Fearless",
            "Thick Hide",
        ],
        "random_mutations": 3,
    },
}


mutations = {
    "Amoeboid": "You're super-duper squeezable.",
    "Amphibian": "You can breathe underwater.",
    "Bite": "You can chew on someone for 1d10 piercing damage.",
    "Blindsight": "You locate creatures within 30 feet of you based on vibrations.",
    "Blue Screen": "You cause robots and machines to malfunction.",
    "Chamaleontic": "Attacks against you from a distance miss more often.",
    "Climber": "You gain a climbing speed equal to your walking speed.",
    "Composite": "You are made of a multitude of smaller creatures.",
    "Constrainer": "You can immobilize foes with the power of your mind.",
    "Darkvision": "You see in the dark within 60 feet of you.",
    "Deadly Eye Ray": "You can channel necrotic energy through your eyes.",
    "Density Controller": (
        "By altering your mass density, you can become tougher or quicker."
    ),
    "Doppelganger": "You can temporarily split into two identical creatures.",
    "Dual Brain": "You shrug off the charmed, frightened or stunned condition easily.",
    "Dwarf": "You are really short.",
    "Ectoplasmic": "You can temporarily become incorporeal.",
    "Elastic": "Your reach increases by 5 ft.",
    "Emberborn": "Deal extra 1d6 fire damage with melee attacks.",
    "Extra Arm*": "Gain an extra arm; can be used to hold weapons or shields.",
    "Fearless": "You are immune to the frightened condition.",
    "Formidable Charisma": "+4 to Charisma score.",
    "Formidable Constitution": "+4 to Constitution score.",
    "Formidable Dexterity": "+4 to Dexterity score.",
    "Formidable Intelligence": "+4 to Intelligence score.",
    "Formidable Strength": "+4 to Strength score.",
    "Formidable Wisdom": "+4 to Wisdom score.",
    "Frenzied Strike": (
        "When fighting with two weapons, add ability mod to second attack damage."
    ),
    "Frostborn": "Deal extra 1d6 cold damage with melee attacks.",
    "Gamma Eyes": "Shoot radiation beams from your eyes.",
    "Gauss Spike": "Manipulate gravity to cause sudden bursts of force.",
    "Giant": "Hold two-handed weapons with one hand.",
    "Greater Saving Throw": "Gain proficiency in a saving throw of your choice.",
    "Horns": "You can gore someone for 2d6 piercing damage.",
    "Hypercognitive": "Give yourself advantage on a single check.",
    "Low-light Vision": "See in dim light as if it were bright light.",
    "Magnetic": "Attacks with metal weapons against you are prone to failure.",
    "Mercurial": (
        "You do not provoke opportunity attacks when moving away from enemies."
    ),
    "Mind Controller": "You can turn enemies against their allies!",
    "Myconid": "As a fungal creature, you can breathe spores.",
    "Natural Killer": "Score critical hits on rolls of 19 or 20; ouch!",
    "Necrotic Touch": "Your touch causes decay.",
    "Nuclear": "You are a walking nuke. Avoid eating beans.",
    "Nightmare": "Enemies are scared by your horrific appearance.",
    "Poison Gas": "Burp a cloud of poison to damage nearby enemies.",
    "Poison Resistance": "You gain resistance to poison damage.",
    "Poisonous Quills": "You can shoot poisonous quills from your body.",
    "Powerful Pheromones": (
        "You have (an unfair) advantage on Charisma (Persuasion) checks."
    ),
    "Prescience": "Use prescience as a reaction to halve damage.",
    "Psychic Resistance": "You gain resistance to psychic damage.",
    "Psychopomp": "Absorb life force from nearby enemies.",
    "Psychic Shield": "When hit by an attack, your mind shields you from harm.",
    "Pulse": "You can travel at light speed, reappearing within 30 feet.",
    "Quick": "+10 feet to all your speeds.",
    "Radiation Resistance": "You are resistant to radiation damage.",
    "Reanimator": "You can reanimate corpses. Man, you do creep me out.",
    "Regeneration": "Regain hit points during combat.",
    "Revitalizing": "You can heal creatures with your touch.",
    "Rooted": "You cannot be knocked prone, and are pushed10 feet less than normal.",
    "Shapeshifter": "You can change your shape into that of any humanoid.",
    "Sonic Burst": "15-foot cone of powerful screech deals 2d6 thunder damage.",
    "Static": "When hit in melee, spend a reaction to deal 2d4lightning to attacker.",
    "Talons": "Your unarmed attack is light and finesse and deals 1d6 slashing damage.",
    "Telepathy": "You can sense and send thoughts within 60 feet of you.",
    "Telekinesis": "You can move objects and push creatures with your mind.",
    "Tentacles": "You may initiate grapples as a bonus action.",
    "Thick Hide": "You gain +2 to Armor Class.",
    "Timewalker": "You can briefly step into the future.",
    "Toughened": "Gain 1 extra Hit Die (counts for starting hit points too! OP!)",
    "Wings": "You gain a flying speed equal to your walking speed.",
    "Wormhole": "Your powers can throw enemies into other dimensions. For some time.",
}

random_skills = [
    "Acrobatics",
    "Animal Handling",
    "Athletics",
    "Conspiracy",
    "Deception",
    "Insight",
    "Intimidation",
    "Investigation",
    "Nature",
    "Perception",
    "Performance",
    "Persuasion",
    "Science",
    "Sleight of Hand",
    "Stealth",
    "Survival",
]

skills = {
    "Acrobatics": "DEX",
    "Ancient Tech": "INT",
    "Animal Handling": "WIS",
    "Athletics": "STR",
    "Conspiracy": "INT",
    "Deception": "CHA",
    "Insight": "WIS",
    "Intimidation": "CHA",
    "Investigation": "INT",
    "Nature": "INT",
    "Perception": "WIS",
    "Performance": "CHA",
    "Persuasion": "CHA",
    "Science": "INT",
    "Sleight of Hand": "DEX",
    "Stealth": "DEX",
    "Survival": "WIS",
}

light_melee = [
    {
        "name": "Knife",
        "damage": "1d8",
        "damage_type": "P",
        "properties": [
            "finesse",
            "light",
        ],
    },
    {
        "name": "Scissors",
        "damage": "1d8",
        "damage_type": "P",
        "properties": [
            "finesse",
            "light",
        ],
    },
    {
        "name": "Scimitar",
        "damage": "1d8",
        "damage_type": "S",
        "properties": [
            "finesse",
            "light",
        ],
    },
    {
        "name": "Machete",
        "damage": "1d8",
        "damage_type": "S",
        "properties": [
            "finesse",
            "light",
        ],
    },
    {
        "name": "Katana",
        "damage": "1d8",
        "damage_type": "S",
        "properties": [
            "finesse",
            "light",
        ],
    },
]

heavy_melee = [
    {
        "name": "Road Sign",
        "damage": "2d6",
        "damage_type": "B",
        "properties": [
            "heavy",
            "two-handed",
        ],
    },
    {
        "name": "Sledgehammer",
        "damage": "2d6",
        "damage_type": "B",
        "properties": [
            "heavy",
            "two-handed",
        ],
    },
    {
        "name": "Chainsaw",
        "damage": "2d6",
        "damage_type": "S",
        "properties": [
            "heavy",
            "two-handed",
        ],
    },
    {
        "name": "Baseball Bat",
        "damage": "2d6",
        "damage_type": "B",
        "properties": [
            "heavy",
            "two-handed",
        ],
    },
    {
        "name": "Greatsword",
        "damage": "2d6",
        "damage_type": "S",
        "properties": [
            "heavy",
            "two-handed",
        ],
    },
]

light_ranged = [
    {
        "name": "Hand Axe",
        "damage": "1d8",
        "damage_type": "S",
        "range": "20/60",
        "properties": [
            "thrown",
        ],
    },
    {
        "name": "Slingshot",
        "damage": "1d8",
        "damage_type": "B",
        "range": "80/320",
        "properties": [],
    },
    {
        "name": "Shuriken",
        "damage": "1d8",
        "damage_type": "P",
        "range": "20/60",
        "properties": [
            "thrown",
        ],
    },
    {
        "name": "Rock",
        "damage": "1d8",
        "damage_type": "B",
        "range": "20/60",
        "properties": [
            "thrown",
        ],
    },
    {
        "name": "Hand Crossbow",
        "damage": "1d8",
        "damage_type": "P",
        "range": "80/320",
        "properties": [],
    },
]

heavy_ranged = [
    {
        "name": "Compound Bow",
        "damage": "1d12",
        "damage_type": "P",
        "range": "100/400",
        "properties": [
            "two-handed",
        ],
    },
    {
        "name": "Heavy Crossbow",
        "damage": "1d12",
        "damage_type": "P",
        "range": "100/400",
        "properties": [
            "two-handed",
        ],
    },
    {
        "name": "Harpoon Gun",
        "damage": "1d12",
        "damage_type": "P",
        "range": "100/400",
        "properties": [
            "two-handed",
        ],
    },
    {
        "name": "Potato Gun",
        "damage": "1d12",
        "damage_type": "B",
        "range": "100/400",
        "properties": [
            "two-handed",
        ],
    },
]

light_gun = [
    {
        "name": "Beretta",
        "damage": "2d6",
        "damage_type": "P",
        "range": "80/320",
        "properties": [
            "ammunition",
        ],
    },
    {
        "name": "Colt",
        "damage": "2d6",
        "damage_type": "P",
        "range": "80/320",
        "properties": [
            "ammunition",
        ],
    },
    {
        "name": "Glock",
        "damage": "2d6",
        "damage_type": "P",
        "range": "80/320",
        "properties": [
            "ammunition",
        ],
    },
    {
        "name": "Desert Eagle",
        "damage": "2d6",
        "damage_type": "P",
        "range": "80/320",
        "properties": [
            "ammunition",
        ],
    },
]

heavy_gun = [
    {
        "name": "Hunting Rifle",
        "damage": "2d10",
        "damage_type": "P",
        "range": "100/400",
        "properties": [
            "ammunition",
            "two-handed",
        ],
    },
    {
        "name": "Shotgun",
        "damage": "2d10",
        "damage_type": "P",
        "range": "100/400",
        "properties": [
            "ammunition",
            "two-handed",
        ],
    },
    {
        "name": "Assault Rifle",
        "damage": "2d10",
        "damage_type": "P",
        "range": "100/400",
        "properties": [
            "ammunition",
            "two-handed",
        ],
    },
    {
        "name": "Bazooka",
        "damage": "2d10",
        "damage_type": "B",
        "range": "100/400",
        "properties": [
            "ammunition",
            "two-handed",
        ],
    },
]

wanderers_pack = [
    "backpack",
    "bedroll",
    "crowbar",
    "duct tape",
    "flashlight",
    "flint and steel",
    "fuel tank (empty)",
    "lock picking tools",
    "canteen",
    "50' rope",
    "tent",
    "trail rations (10 days)",
]

scavenged_junk = [
    "vacuum cleaner",
    "special contents DVD from a horror movie",
    "wireless mouse",
    "office chair",
    "plastic mug: 'I \u2764 Caffeine'",
    "umbrella",
    "biker helmet",
    "tennis racket",
    "sunglasses",
    "DVD player/recorder",
    "body bag",
    "t-shirt with the FunCorp logo",
    "TV screen",
    f"{roll_dice(3, 4)} crayons",
    "8gb USB flash drive",
    "car stereo",
    f"{roll_dice(1, 4)} winter tires",
    "beer, 6-pack",
    "superglue",
    "earphones",
    "snow boots",
    "printer",
    f"toy {random.choice(['car','car','truck','airplane','helicopter','space shuttle'])}",  # noqa: E501
    "matches",
    "mini fridge",
    "solar power generator",
    "pickup truck",
    "bikini",
    "5 cans of tuna",
    "steel mirror",
    "canoe with 1 oar",
    "punching bag",
    "fuel tank (1 gallon, full)",
    "deck of cards",
    "bottle of ink",
    "ammunition",
    "handheld mosquito zapper",
    "digital thermometer",
    "wheelchair",
    "bottle of lubricant",
    "skateboard",
    "dictionary",
    "electric wire (20')",
    "kaleidoscope",
    "pajamas",
    "personal computer",
    "handcuffs, pink and hairy",
    "desk lamp",
    "webcam",
    "joystick",
    "rubber gloves",
    "binoculars",
    "DIY manual",
    f"{random.choice(['ghost','ghost','zombie','zombie','witch','vampire'])} halloween costume",  # noqa: E501
    "carpet",
    "box of diapers",
    "electric blender",
    "wooden ladder",
    "gas grill",
    "bottle of curry sauce",
    "leather jacket",
    "baseball hat",
    "wristwatch",
    "film projector",
    "inflatable air bed",
    "cell phone",
    "motorcycle",
    "wrestling mask",
    "novelty tiger skin rug",
    "toothbrush",
    "teddy bear",
    "30 lb. dumbell",
    "pair of rollerblades",
    "electric guitar",
    "bottle of shampoo",
    "hockey stick",
    "bird cage",
    "pool cue",
    "string of christmas lights (50')",
    "remote control",
    "air compressor",
    f"bottle of {random.choice(['red','white'])} wine",
    "tire iron",
    "trash can",
    "comic book",
    "green plastic soldiers",
    "toy water pistol",
    "bonsai tree",
    "boxing gloves",
    f"package of {random.choice(['mint','mint','strawberry','strawberry','orange','banana'])} gum",  # noqa: E501
    "wireless router",
    "electric fan",
    f"box of {roll_dice(2, 4)} cigars",
    "lawn mover",
    "box of toilet paper",
]

ancient_gear = [
    "bio-scanner",
    "telepathic parrot",
    "hypnotic ray",
    "animatronic dog",
    "security drone",
    "stun baton",
    "energy mace",
    "shield generator",
    "vibro-knife",
    "food synthesizer",
    "laser pistol",
    "antigravity belt",
    "power armor",
    "pulse rifle",
    "plasma gun",
    "plasma saw",
    "gamma field generator",
    "panacea injector",
    "flamethrower",
    "evil death ray",
]
