from rpg_tools.maze_rats.char import PlayerCharacter


def test_character_creation():
    c = PlayerCharacter()
    assert hasattr(c, "name")
    assert hasattr(c, "abilities")
    assert hasattr(c, "hp")
    assert hasattr(c, "weapons")


def test_character_abilities_method_2():
    c = PlayerCharacter(abilities_method=2)
    assert len(c.abilities) == 3


def test_character_to_dict():
    c = PlayerCharacter()
    d = c.to_dict()
    assert isinstance(d, dict)
