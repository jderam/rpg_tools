races = {
    'Human': {
        'hp': 6,
        'trait': {'RANDOM': 'Select an additional Trait from the Trait List.'},
        },
    'Dwarf': {
        'hp': 8,
        'trait': {'Dark Vision': 'You are able to see 30 feet around you in total darkness.'},
    },
    'Fey': {
        'hp': 6,
        'trait': {'Bow Mastery': 'You have Mastered bows and have Advantage when using them. This is in addition to the Mastered weapon chosen at Adventurer Creation.'},
    },
    'Goblin': {
        'hp': 4,
        'trait': {'Goblin Agility': 'You can Test 1d6 whenever you are successfully hit by an enemy. If your Test is successful, you evade the attack and do not take damage. Declaring Evade as an Action has no additional benefit.'},
    },
    'Salimar': {
        'hp': 5,
        'trait': {'Pyrothermic Healing': 'Any amount of damage that would be dealt to you by a source of fire instead heals you for that amount.'},
    },
}


traits = {
    'Acrobat': "It's up there? No problem! You gain Advantage when Testing to do acrobatic tricks such as tumbling, long-distance jumps, climbing, and maintaining balance.",
    'Alchemist': "Dragon's blood has many uses. It's also great on salads. Provided the right reagents and recipes, you can mix potions, elixirs, and poisons. You also gain Advantage when identifying unknown liquids.",
    'Beastspeaker': "What is it, boy?! The king fell down a well?! You are able to communicate with animals. This form of communication is primitive and very simplistic.",
    'Berserker': "YAAAARRRRRGHHH! When making a melee attack, you can choose to attack at a Disadvantage. If the attack is successful, it deals 2 points of damage.",
    'Brawler': "Everybody has a plan until they get punched in the face. You gain Advantage when making unarmed attacks.",
    'Diehard': "I'm not going down that easy. When an attack would reduce you to 0 Hit Points, it instead reduces you to 1 Hit Point. You can do this once per day.",
    'Charismatic': "I can get what I want without even asking. You gain Advantage when attempting to convince someone of something or otherwise influence them.",
    'Dungeoneer': "We go left. I can tell by some of the moss and from seeing a lot of dungeons in my time. You gain Advantage when attempting to find your way through a dungeon or cave system, and when attempting to identify creatures native to dungeons or caves.",
    'Educated': "I didn't go to academy for four years for nothing. You gain Advantage when checking to see if you know specific information.",
    'Eidetic Memory': "You remember that guy in that city? Who did that thing? What did he say? When Testing to recall information you have seen or heard previously – even in passing – you succeed on a roll of 4, 5, or 6.",
    'Familiar': "Your faceless shadow cat is really freaking me out, man. For as long as you can remember, you have never truly been alone. Another spirit has linked itself to yours, accepting you as its friend and master. (See Magic)",
    'Fleet of Foot': "Running away is always a valid option. Your speed increases from 25 feet to 30 feet.",
    'Healer': "I've seen worse, son. You'll pull through. As an Action, you can Test 2d6 to heal a creature other than yourself. If the Test is successful, the target creature is healed for 2 Hit Points. This Trait can also be used to cure poison, disease, and other physical ailments that are non-magical. You must be next to the creature to heal it.",
    'Insightful': "Not sure if serious... You gain Advantage when Testing to discern whether or not someone is telling the truth or lying.",
    'Marksman': "The odds of hitting your target increase dramatically when you aim at it. When you Focus, your next attack with a ranged weapon is successful on a Test of 3, 4, 5, or 6.",
    'Nimble Fingers': "I could have sworn I left it right here! You gain Advantage when Testing to pick locks, pick pockets, or steal.",
    'Opportunist': "One man's failure is another man's opening to stab the idiot who failed. If an enemy within range fails to hit with an attack against you, you may immediately make an attack with Disadvantage against that enemy.",
    'Perceptive': "What has been seen cannot be unseen. You gain Advantage when Testing to gain information about your surroundings or find things which may be hidden. You gain this even while asleep.",
    'Quick Shot': "Pew, pew, pew! You are able to reload a Ranged Weapon and fire it in one Action.",
    'Resolute': "I will not be a casualty of fear. You gain Advantage on all Save Tests.",
    'Shield Bearer': "I've got you covered. While wielding a shield, Test with 2d6 on Evade or Goblin Agility Actions instead of 1d6. If you choose this Trait, your Adventurer gains a shield at Adventurer creation.",
    'Sneaky': "Silent, but deadly. You gain Advantage when Testing to hide or sneak around without others noticing you.",
    'Spell Reader': "P as in phylactery. You have spent years learning the sacred language of the arcane, allowing you to read power-laced words from magic scrolls. (See Magic)",
    'Spell-Touched': "It runs in the family. You were born with an arcane heritage, and while the centuries have diluted the power, you are still able to subtly influence the world around you by merely willing it to happen. (See Magic)",
    'Strong': "Forget the doorknob! Stand back, I'll kick it in! You gain Advantage when Testing to do something with brute force.",
    'Survivalist': "These berries are safe to eat... I think. You gain Advantage when Testing to forage for food, find water, seek shelter, or create shelter in the wild.",
    'Tough': "I have not journeyed all this way because I am made of sugar candy. You gain 1 additional Hit Point.",
    'Tracker': "These prints are fresh. He went that way. You gain Advantage when Testing to track someone or an animal in the wilderness. While outside, you can also locate true north without Testing.",
    'Trapmaster': "It's a trap! You gain Advantage when Testing to create, locate, and disarm traps.",
    'Vigilant': "Better to stay ready than to get ready. You gain Advantage on Initiative Tests.",
}

weapon_proficiencies = [
    'Light Melee',
    'Heavy Melee',
    'Ranged',
]

light_weapons = [
    'Dagger',
    'Short Sword',
    'Hand Axe',
    'Rapier',
    'Mace',
    'Staff',
    'Club',
]

heavy_weapons = [
    'Great Sword',
    'War Axe',
    'Spear',
    'Polearm',
    'Two-handed Flail',
    'War Hammer',
]

ranged_weapons = [
    'Sling',
    'Crossbow',
    'Bow',
]

common_items = [
    'Backpack',
    'Barrel',
    'Bedroll',
    'Bottle',
    'Candle',
    'Chest',
    'Clay Jug',
    'Cloak',
    'Crowbar',
    'Firewood',
    'Fishing Rod',
    'Flask',
    'Flint & Steel',
    'Grappling Hook',
    'Ink Pen',
    'Ink',
    'Lantern',
    'Mug',
    'Musical Instrument',
    'Pint of Oil',
    'Paper (10 sheets)',
    'Parchment (5 sheets)',
    'Belt Pouch',
    'Rations (7 days)',
    'Rope (50 feet)',
    'Rucksack',
    'Sealing Wax',
    'Sewing Needle & Thread',
    'Shovel',
    'Torch',
    'Empty Waterskin',
]

uncommon_items = [
    'Alchemical Reagents',
    'Healing Potion',
    'Lock Pick Set',
    'Minor Magic Scrolls',
    'Mirror',
    'Personal Tent',
    'Shield',
]

rare_items = [
    'Disguise Kit',
    'Forged Documents',
    'Hourglass',
    'Major Magic Scroll',
    'Simple Magical Items',
    'Spyglass',
    'Vial of Poison,'
]

adventurers_kit = [
    'Bedroll',
    'Flint & Steel',
    'Belt Pouch',
    'Rucksack',
    'Lantern',
    'Waterskin (empty)',
    'Oil (3 pints)',
    'Rope (50 feet)',
    'Rations (7 days)',
    'Torch',
    'Cloak',
]
