races = {
    "Human": {
        "hp": 6,
        "trait": {"RANDOM": "Select an additional Trait from the Trait List."},
    },
    "Dwarf": {
        "hp": 8,
        "trait": {
            "Dark Vision": "You are able to see 30 feet around you in total darkness."
        },
    },
    "Fey": {
        "hp": 6,
        "trait": {
            "Bow Mastery": (
                "You have Mastered bows and have Advantage when using them. "
                "This is in addition to the Mastered weapon chosen at "
                "Adventurer Creation."
            )
        },
    },
    "Goblin": {
        "hp": 4,
        "trait": {
            "Goblin Agility": (
                "You can Test 1d6 whenever you are successfully hit by an enemy. "
                "If your Test is successful, you evade the attack and do not take "
                "damage. Declaring Evade as an Action has no additional benefit."
            )
        },
    },
    "Salimar": {
        "hp": 5,
        "trait": {
            "Pyrothermic Healing": (
                "Any amount of damage that would be dealt to you by a source of "
                "fire instead heals you for that amount."
            )
        },
    },
}


traits = [
    {
        "name": "Acrobat",
        "flavor_text": "It's up there? No problem!",
        "description": (
            "You gain Advantage when Testing to do acrobatic tricks such as tumbling, "
            "long-distance jumps, climbing, and maintaining balance."
        ),
    },
    {
        "name": "Alchemist",
        "flavor_text": "Dragon's blood has many uses. It's also great on salads.",
        "description": (
            "Provided the right reagents and recipes, you can mix potions, elixirs, "
            "and poisons. You also gain Advantage when identifying unknown liquids."
        ),
    },
    {
        "name": "Beastspeaker",
        "flavor_text": "What is it, boy?! The king fell down a well?!",
        "description": (
            "You are able to communicate with animals. This form of communication "
            "is primitive and very simplistic."
        ),
    },
    {
        "name": "Berserker",
        "flavor_text": "YAAAARRRRRGHHH!",
        "description": (
            "When making a melee attack, you can choose to attack at a Disadvantage. "
            "If the attack is successful, it deals 2 points of damage."
        ),
    },
    {
        "name": "Brawler",
        "flavor_text": "Everybody has a plan until they get punched in the face.",
        "description": "You gain Advantage when making unarmed attacks.",
    },
    {
        "name": "Diehard",
        "flavor_text": "I'm not going down that easy.",
        "description": (
            "When an attack would reduce you to 0 Hit Points, it instead reduces you "
            "to 1 Hit Point. You can do this once per day."
        ),
    },
    {
        "name": "Charismatic",
        "flavor_text": "I can get what I want without even asking.",
        "description": (
            "You gain Advantage when attempting to convince someone of something "
            "or otherwise influence them."
        ),
    },
    {
        "name": "Dungeoneer",
        "flavor_text": "We go left. I can tell by some of the moss and from seeing a lot of dungeons in my time.",
        "description": (
            "You gain Advantage when attempting to find your way through a dungeon or cave "
            "system, and when attempting to identify creatures native to dungeons or caves."
        ),
    },
    {
        "name": "Educated",
        "flavor_text": "I didn't go to academy for four years for nothing.",
        "description": "You gain Advantage when checking to see if you know specific information.",
    },
    {
        "name": "Eidetic Memory",
        "flavor_text": "You remember that guy in that city? Who did that thing? What did he say?",
        "description": (
            "When Testing to recall information you have seen or heard previously – even "
            "in passing – you succeed on a roll of 4, 5, or 6."
        ),
    },
    {
        "name": "Familiar",
        "flavor_text": "Your faceless shadow cat is really freaking me out, man.",
        "description": (
            "For as long as you can remember, you have never truly been alone. "
            "Another spirit has linked itself to yours, accepting you as its "
            "friend and master. (See Magic)"
        ),
    },
    {
        "name": "Fleet of Foot",
        "flavor_text": "Running away is always a valid option.",
        "description": "Your speed increases from 25 feet to 30 feet.",
    },
    {
        "name": "Healer",
        "flavor_text": "I've seen worse, son. You'll pull through.",
        "description": (
            "As an Action, you can Test 2d6 to heal a creature other than yourself. "
            "If the Test is successful, the target creature is healed for 2 Hit Points. "
            "This Trait can also be used to cure poison, disease, and other physical ailments "
            "that are non-magical. You must be next to the creature to heal it."
        ),
    },
    {
        "name": "Insightful",
        "flavor_text": "Not sure if serious...",
        "description": (
            "You gain Advantage when Testing to discern whether someone is telling the truth or lying."
        ),
    },
    {
        "name": "Marksman",
        "flavor_text": "The odds of hitting your target increase dramatically when you aim at it.",
        "description": "When you Focus, your next attack with a ranged weapon is successful on a Test of 3, 4, 5, or 6.",
    },
    {
        "name": "Nimble Fingers",
        "flavor_text": "I could have sworn I left it right here!",
        "description": "You gain Advantage when Testing to pick locks, pick pockets, or steal.",
    },
    {
        "name": "Opportunist",
        "flavor_text": "One man's failure is another man's opening to stab the idiot who failed.",
        "description": (
            "If an enemy within range fails to hit with an attack against you, you may "
            "immediately make an attack with Disadvantage against that enemy."
        ),
    },
    {
        "name": "Perceptive",
        "flavor_text": "What has been seen cannot be unseen.",
        "description": (
            "You gain Advantage when Testing to gain information about your surroundings or "
            "find things which may be hidden. You gain this even while asleep."
        ),
    },
    {
        "name": "Quick Shot",
        "flavor_text": "Pew, pew, pew!",
        "description": "You are able to reload a Ranged Weapon and fire it in one Action.",
    },
    {
        "name": "Resolute",
        "flavor_text": "I will not be a casualty of fear.",
        "description": "You gain Advantage on all Save Tests.",
    },
    {
        "name": "Shield Bearer",
        "flavor_text": "I've got you covered.",
        "description": (
            "While wielding a shield, Test with 2d6 on Evade or Goblin Agility Actions instead of 1d6. "
            "If you choose this Trait, your Adventurer gains a shield at Adventurer creation."
        ),
    },
    {
        "name": "Sneaky",
        "flavor_text": "Silent, but deadly.",
        "description": "You gain Advantage when Testing to hide or sneak around without others noticing you.",
    },
    {
        "name": "Spell Reader",
        "flavor_text": "P as in phylactery.",
        "description": (
            "You have spent years learning the sacred language of the arcane, allowing you "
            "to read power-laced words from magic scrolls. (See Magic)"
        ),
    },
    {
        "name": "Spell-Touched",
        "flavor_text": "It runs in the family.",
        "description": (
            "You were born with an arcane heritage, and while the centuries have diluted the power, "
            "you are still able to subtly influence the world around you by merely willing it to happen. (See Magic)"
        ),
    },
    {
        "name": "Strong",
        "flavor_text": "Forget the doorknob! Stand back, I'll kick it in!",
        "description": "You gain Advantage when Testing to do something with brute force.",
    },
    {
        "name": "Survivalist",
        "flavor_text": "These berries are safe to eat... I think.",
        "description": (
            "You gain Advantage when Testing to forage for food, find water, seek shelter, "
            "or create shelter in the wild."
        ),
    },
    {
        "name": "Tough",
        "flavor_text": "I have not journeyed all this way because I am made of sugar candy.",
        "description": "You gain 1 additional Hit Point.",
    },
    {
        "name": "Tracker",
        "flavor_text": "These prints are fresh. He went that way.",
        "description": (
            "You gain Advantage when Testing to track someone or an animal in the wilderness. "
            "While outside, you can also locate true north without Testing."
        ),
    },
    {
        "name": "Trapmaster",
        "flavor_text": "It's a trap!",
        "description": "You gain Advantage when Testing to create, locate, and disarm traps.",
    },
    {
        "name": "Vigilant",
        "flavor_text": "Better to stay ready than to get ready.",
        "description": "You gain Advantage on Initiative Tests.",
    },
]

weapon_proficiencies = [
    "Light Melee",
    "Heavy Melee",
    "Ranged",
]

light_weapons = [
    "Dagger",
    "Short Sword",
    "Hand Axe",
    "Rapier",
    "Mace",
    "Staff",
    "Club",
]

heavy_weapons = [
    "Great Sword",
    "War Axe",
    "Spear",
    "Polearm",
    "Two-handed Flail",
    "War Hammer",
]

ranged_weapons = [
    "Sling",
    "Crossbow",
    "Bow",
]

common_items = [
    "Backpack",
    "Barrel",
    "Bedroll",
    "Bottle",
    "Candle",
    "Chest",
    "Clay Jug",
    "Cloak",
    "Crowbar",
    "Firewood",
    "Fishing Rod",
    "Flask",
    "Flint & Steel",
    "Grappling Hook",
    "Ink Pen",
    "Ink",
    "Lantern",
    "Mug",
    "Musical Instrument",
    "Pint of Oil",
    "Paper (10 sheets)",
    "Parchment (5 sheets)",
    "Belt Pouch",
    "Rations (7 days)",
    "Rope (50 feet)",
    "Rucksack",
    "Sealing Wax",
    "Sewing Needle & Thread",
    "Shovel",
    "Torch",
    "Empty Waterskin",
]

uncommon_items = [
    "Alchemical Reagents",
    "Healing Potion",
    "Lock Pick Set",
    "Minor Magic Scrolls",
    "Mirror",
    "Personal Tent",
    "Shield",
]

rare_items = [
    "Disguise Kit",
    "Forged Documents",
    "Hourglass",
    "Major Magic Scroll",
    "Simple Magical Items",
    "Spyglass",
    "Vial of Poison,",
]

adventurers_kit = [
    "Bedroll",
    "Flint & Steel",
    "Belt Pouch",
    "Rucksack",
    "Lantern",
    "Waterskin (empty)",
    "Oil (3 pints)",
    "Rope (50 feet)",
    "Rations (7 days)",
    "Torch",
    "Cloak",
]
