import random


physical_effects = [
    "Animating",
    "Attracting",
    "Binding",
    "Blossoming",
    "Consuming",
    "Creeping",
    "Crushing",
    "Diminishing",
    "Dividing",
    "Duplicating",
    "Enveloping",
    "Expanding",
    "Fusing",
    "Grasping",
    "Hastening",
    "Hindering",
    "Illuminating",
    "Imprisoning",
    "Levitating",
    "Opening",
    "Pertifying",
    "Phasing",
    "Piercing",
    "Pursuing",
    "Reflecting",
    "Regenerating",
    "Rending",
    "Repelling",
    "Resurrecting",
    "Screaming",
    "Sealing",
    "Shapeshifting",
    "Shielding",
    "Spawning",
    "Transmuting",
    "Transporting",
]

physical_elements = [
    "Acid",
    "Amber",
    "Bark",
    "Blood",
    "Bone",
    "Brine",
    "Clay",
    "Crow",
    "Crystal",
    "Ember",
    "Flesh",
    "Fungus",
    "Glass",
    "Honey",
    "Ice",
    "Insect",
    "Wood",
    "Lava",
    "Moss",
    "Obsidian",
    "Oil",
    "Poison",
    "Rat",
    "Salt",
    "Sand",
    "Sap",
    "Serpent",
    "Slime",
    "Stone",
    "Tar",
    "Thorn",
    "Vine",
    "Water",
    "Wine",
    "Wood",
    "Worm",
]

physical_forms = [
    "Altar",
    "Armor",
    "Arrow",
    "Beast",
    "Blade",
    "Cauldron",
    "Chain",
    "Chariot",
    "Claw",
    "Cloak",
    "Colossus",
    "Crown",
    "Elemental",
    "Eye",
    "Fountain",
    "Gate",
    "Golem",
    "Hammer",
    "Horn",
    "Key",
    "Mask",
    "Monolith",
    "Pit",
    "Prison",
    "Sentinel",
    "Servant",
    "Shield",
    "Spear",
    "Steed",
    "Swarm",
    "Tentacle",
    "Throne",
    "Torch",
    "Trap",
    "Wall",
    "Web",
]

etherial_effects = [
    "Avenging",
    "Banishing",
    "Bewildering",
    "Blinding",
    "Charming",
    "Communicating",
    "Compelling",
    "Concealing",
    "Deafening",
    "Deceiving",
    "Deciphering",
    "Disgusting",
    "Dispelling",
    "Emboldening",
    "Encoding",
    "Energizing",
    "Enlightening",
    "Enraging",
    "Excruciating",
    "Foreseeing",
    "Intoxicating",
    "Maddening",
    "Mesmerizing",
    "Mindreading",
    "Nullifying",
    "Paralyzing",
    "Revealing",
    "Revolting",
    "Scrying",
    "Silencing",
    "Soothing",
    "Summoning",
    "Terrifying",
    "Warding",
    "Wearying",
    "Withering",
]

etherial_elements = [
    "Ash",
    "Chaos",
    "Distortion",
    "Dream",
    "Dust",
    "Echo",
    "Ectoplasm",
    "Fire",
    "Fog",
    "Ghost",
    "Harmony",
    "Heat",
    "Light",
    "Lightning",
    "Memory",
    "Mind",
    "Mutation",
    "Negation",
    "Plague",
    "Plasma",
    "Probability",
    "Rain",
    "Rot",
    "Shadow",
    "Smoke",
    "Snow",
    "Soul",
    "Star",
    "Stasis",
    "Steam",
    "Thunder",
    "Time",
    "Void",
    "Warp",
    "Whisper",
    "Wind",
]

etherial_forms = [
    "Aura",
    "Beacon",
    "Beam",
    "Blast",
    "Blob",
    "Bolt",
    "Bubble",
    "Call",
    "Cascade",
    "Circle",
    "Cloud",
    "Coil",
    "Cone",
    "Cube",
    "Dance",
    "Disk",
    "Field",
    "Form",
    "Gaze",
    "Loop",
    "Moment",
    "Nexus",
    "Portal",
    "Pulse",
    "Pyramid",
    "Ray",
    "Shard",
    "Sphere",
    "Spray",
    "Storm",
    "Swarm",
    "Torrent",
    "Touch",
    "Vortex",
    "Wave",
    "Word",
]


def generate_spell():
    combinations = [
        [physical_effects, physical_forms],
        [physical_effects, etherial_forms],
        [etherial_effects, physical_forms],
        [etherial_effects, etherial_forms],
        [physical_elements, physical_forms],
        [physical_elements, etherial_forms],
        [etherial_elements, physical_forms],
        [etherial_elements, etherial_forms],
        [physical_effects, physical_elements],
        [physical_effects, etherial_elements],
        [etherial_effects, physical_elements],
        [etherial_effects, etherial_elements],
    ]
    tables = random.choice(combinations)
    part_a = random.choice(tables[0])
    part_b = random.choice(tables[1])
    spell = f"{part_a} {part_b}"
    return spell