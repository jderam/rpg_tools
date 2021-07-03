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
        "speed": "30', Fly 30'",
        "skills": [
            "Perception",
        ],
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
        "speed": "40'",
        "skills": [
            "Stealth",
        ],
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
        "speed": "30', Climb 30'",
        "skills": [
            "Survival",
        ],
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
        "speed": "30'",
        "skills": [
            "random",
        ],
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
        "speed": "30'",
        "skills": [
            "Ancient Tech",
            "random",
        ],
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
        "speed": "25'",
        "skills": [
            "Nature",
        ],
        "features": [{"Flammable: Vulnerable to fire damage"}],
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
        "speed": "30'",
        "skills": [
            "Investigation",
        ],
        "features": [
            {
                "Tin Man": (
                    "You're not considered a living creature, and do not need to eat, "
                    "drink, breathe or sleep. You can eat or drink if you want. In "
                    "addition, you are immune to radiation, poison and poison damage, "
                    "disease, and petrification. You cannot be put to sleep. You do, "
                    "however, take short and long rests (cooling down your systems), "
                    "are unconscious when at 0 hp (you can be stabilized with a DC 10 "
                    "Intelligence (Science) check); you are destroyed (which means "
                    "your character 'dies') if you fail three death saves or take "
                    "massive damage."
                )
            }
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
        "speed": "30'",
        "skills": [
            "Intimidation",
        ],
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
