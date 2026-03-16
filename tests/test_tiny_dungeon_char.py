from rpg_tools.tiny_dungeon.char import PlayerCharacter


def test_character_creation():
    c = PlayerCharacter()
    assert hasattr(c, "race")
    assert hasattr(c, "hp")
    assert hasattr(c, "traits")
    assert hasattr(c, "weapon_proficiency")
    assert hasattr(c, "equipment")


def test_character_specific_race():
    c = PlayerCharacter("dwarf")
    assert c.race == "Dwarf"


def test_character_invalid_race():
    c = PlayerCharacter("notarace")
    # Should fall back to a random valid race
    assert c.race is not None
    assert c.hp > 0


def test_character_to_dict():
    c = PlayerCharacter()
    d = c.to_dict()
    assert isinstance(d, dict)
