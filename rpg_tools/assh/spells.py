assh_magician_spells = {
    1: [
        "Alarm",
        "Burning Hands",
        "Charm Person",
        "Dancing Lights",
        "Dash",
        "Decipher Language",
        "Detect Magic",
        "Enlargement",
        "Feather Fall",
        "Floating Disc",
        "Friends",
        "Grease",
        "Hold Portal",
        "Identify",
        "Influence Normal Fire",
        "Jump",
        "Light",
        "Magic Missile",
        "Melt Ice",
        "Mending",
        "Message",
        "Mount",
        "Protection from Evil",
        "Shield",
        "Shocking Grasp",
        "Shove",
        "Sleep",
        "Sorcerer Mark",
        "Sorcerous Armour",
        "Spider Climb",
        "Unseen Servant",
        "Ventriloquism",
        "Write Spell",
    ]
}

assh_cleric_spells = {
    1: [
        "Bless",
        "Bless Oil or Water",
        "Ceremony of Consecration",
        "Cold Resistance",
        "Command",
        "Create Water",
        "Cure Light Wounds",
        "Detect Evil",
        "Detect Magic",
        "Detect Malady",
        "Light",
        "Magic Stone",
        "Omen",
        "Perceive Disguise",
        "Precipitate",
        "Protection from Evil",
        "Purify Food and Drink",
        "Remove Fear",
        "Sanctuary",
    ]
}

dying_earth_spells = {
    "Offensive": [
        {
            "name": "The Charm of Appersonation",
            "range": "0",
            "duration": "2-12 rounds +2/lvl",
            "aoe": "Caster",
            "save": "None",
            "description": (
                "Alter appearance and clothing to any humanoid figure. Cannot mimic "
                "specific individuals."
            ),
        },
        {
            "name": "Evard's Frictionless Field",
            "range": '1"',
            "duration": "3 rounds + 1/level",
            "aoe": '1" square',
            "save": "Special",
            "description": (
                "Save vs. spell or slip and fall. If cast on item then save or drop "
                "immediately."
            ),
        },
        {
            "name": "The Hypnotic Charm",
            "range": '12"',
            "duration": "Special",
            "aoe": "1 person",
            "save": "Negates",
            "description": "Target regards caster as trusted friend and ally.",
        },
        {
            "name": "The Importunate Insult",
            "range": '3"',
            "duration": "Instantaneous",
            "aoe": "2 HD/caster level",
            "save": "Negates",
            "description": (
                "Target rushes to attack magic-user in rage, attacking melee only."
            ),
        },
        {
            "name": "The Kaleidoscopic Spray",
            "range": "0",
            "duration": "Instantaneous",
            "aoe": '1⁄2"x2"x2" wedge',
            "save": "Special",
            "description": (
                "Vivid colour spray affects 1d6 creatures. Caster level or below: "
                "unconscious 2-8 rounds. 1-2 levels higher: blind 1-4 rounds. 3 or "
                "more levels higher: stunned for 1 round. 6 HD or more gets a saving "
                "throw."
            ),
        },
        {
            "name": "Kazimir's Rsplendent Coutre",
            "range": "0",
            "duration": "1 hour/level",
            "aoe": "Caster",
            "save": "None",
            "description": (
                "Dazzlingly fashionable apparel, gain 2-8 charisma and viewers make "
                "immediate reaction checks, become impressed or jealous/irritated."
            ),
        },
        {
            "name": "Laeral's Baleful Aura",
            "range": '3"',
            "duration": "1 round",
            "aoe": "Caster",
            "save": "Negates",
            "description": (
                "Become unquantifiably terrifying; friends & foes save vs. magic or "
                "flee 1-3 rounds."
            ),
        },
        {
            "name": "The Metamorphoun of Fire",
            "range": '1/2"/level',
            "duration": "2 rounds/level",
            "aoe": '1" radius',
            "save": "None",
            "description": (
                "Increase fires up to double size/heat or down to embers, spread onto "
                "any burnable material, or snuff out all fires entirely."
            ),
        },
        {
            "name": "Sirrian's Aggrandisement",
            "range": '1⁄2"/level',
            "duration": "1 turn/level",
            "aoe": "<10 cubic feet/lvl",
            "save": "Negates",
            "description": (
                "Increase or decrease target's size up to 200%, Strength & damage "
                "change proportionately."
            ),
        },
        {
            "name": "The Spell of Exquisite Repose",
            "range": '3" + 1"/level',
            "duration": "5 rounds/level",
            "aoe": '3" diameter',
            "save": "None",
            "description": "Cause comatose slumber, awaken only if slapped/wounded.",
        },
    ],
    "Defensive": [
        {
            "name": "The Apotropaic Circle",
            "range": "Touch",
            "duration": "2 rounds/level",
            "aoe": '<1" diameter',
            "save": "None",
            "description": (
                "Trace a circle in powdered silver; blocks all conjured & extraplanar "
                "creatures and possession attempts."
            ),
        },
        {
            "name": "The Audible Glamer",
            "range": '6" + 1"/level',
            "duration": "2 rounds/level",
            "aoe": "Hearing range",
            "save": "None",
            "description": "Create auditory-only illusion.",
        },
        {
            "name": "The Effervescent Lights of Kwalish",
            "range": '4" + 1"/level',
            "duration": "1 turn/level",
            "aoe": "Special",
            "save": "None",
            "description": (
                "Create A) 1-4 lights resembling torches, B) glowing spheres (as "
                "will-o-wisp), C) faintly glowing man-like shape. Moves as directed."
            ),
        },
        {
            "name": "The Expeditious Retreat",
            "range": "0",
            "duration": "3 rounds + 1/level",
            "aoe": "Caster",
            "save": "None",
            "description": (
                "Triple movement, running jumps 30' forward or 10' up, cannot take "
                "any other action while moving."
            ),
        },
        {
            "name": "The Heavenly Screen",
            "range": '3"',
            "duration": "2-8 rounds + 1/lvl",
            "aoe": '2" cube/level',
            "save": "None",
            "description": "Veil of silvery mist obscures vision beyond 2'.",
        },
        {
            "name": "The Howling Rune",
            "range": '1"',
            "duration": "4 hours + 1/level",
            "aoe": "1 object/creature",
            "save": "Negates",
            "description": (
                "Target erupts in involuntary screaming (see Shrieker) when creature "
                "approaches within 10'."
            ),
        },
        {
            "name": "The Imperturbable Quiescent Sphere",
            "range": "0",
            "duration": "5 rounds/level",
            "aoe": "Caster",
            "save": "None",
            "description": (
                "Invisible barrier gives AC 17 vs. missiles, AC 15 vs. other attacks."
            ),
        },
        {
            "name": "Isain's Fortuitous Interruption",
            "range": '1"/level',
            "duration": "1 second/level",
            "aoe": "Special",
            "save": "None",
            "description": (
                "200 lb + 200 per caster level assumes mass of a feather, no falling "
                "damage."
            ),
        },
        {
            "name": "The Lesser Sign of Sealing",
            "range": '2"/level',
            "duration": "Permanent",
            "aoe": "80 square feet/lvl",
            "save": "None",
            "description": "Seal door or gate as if securely barred and locked.",
        },
        {
            "name": "Otto's Arachnid Grip",
            "range": "Touch",
            "duration": "3 rounds +1/level",
            "aoe": "1 creature",
            "save": "Negates",
            "description": (
                'Climb vertical surfaces/ceilings at 3". Objects less than 5 lbs. '
                "stick to hands."
            ),
        },
    ],
    "Miscellaneous": [
        {
            "name": "The Abstention of the Written Path",
            "range": '6"',
            "duration": "1 turn",
            "aoe": '1"x1" area/round',
            "save": "None",
            "description": "Detect secret passages, portals and openings.",
        },
        {
            "name": "The Call to the Familiar Spirit",
            "range": "Special",
            "duration": "Special",
            "aoe": "Special",
            "save": "None",
            "description": (
                "Burn 1000 sp incense, herbs & fat, incantation lasting 24 hours. "
                "Summons familiar."
            ),
        },
        {
            "name": "The Call to the Unseen Servant",
            "range": "0",
            "duration": "6 turns + 1/level",
            "aoe": "Special",
            "save": "None",
            "description": (
                'Invisible creature acts as valet, servant etc. AC 15, MV 18", HD 2; '
                "bound to obey caster but will not fight on their behalf. If abused "
                "seeks to pervert instructions."
            ),
        },
        {
            "name": "The Discerner of Enchantments",
            "range": '6"',
            "duration": "2 rounds/level",
            "aoe": '1" path',
            "save": "None",
            "description": "Detect magic and intensity.",
        },
        {
            "name": "The Indelible Emblem",
            "range": "Touch",
            "duration": "Permanent",
            "aoe": "<1 square foot",
            "save": "None",
            "description": (
                "Inscribes personal mark and 6 other characters, visible or invisible."
            ),
        },
        {
            "name": "Melf's Impermeable Membrane",
            "range": "Touch",
            "duration": "24 hours",
            "aoe": "<10 cubic feet/lvl",
            "save": "None",
            "description": "Repel all liquid from subject.",
        },
        {
            "name": "Nahal's Reckless Dweomer",
            "range": "Special",
            "duration": "Special",
            "aoe": "Special",
            "save": "Special",
            "description": (
                "Attempt to cast any spell in spellbook; roll results on Wild Surge "
                "table."
            ),
        },
        {
            "name": "Phandaal's Polyglottal Lobe",
            "range": "Touch",
            "duration": "5 rounds/level",
            "aoe": "1 object/creature",
            "save": "None",
            "description": "Understand and speak any one language.",
        },
        {
            "name": "The Spell of Pragmatic Amalgamation",
            "range": '3"',
            "duration": "Permanent",
            "aoe": "5'x5' / level",
            "save": "None",
            "description": "Mend or rejoin broken objects.",
        },
        {
            "name": "Tenser's Floating Disc",
            "range": '2"',
            "duration": "3 turns + 1/level",
            "aoe": "Special",
            "save": "None",
            "description": (
                "Floating null-gravity plane supports 100 lb per level, moves as "
                "directed."
            ),
        },
    ],
}
