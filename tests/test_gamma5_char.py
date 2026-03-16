from rpg_tools.gamma5.char import PlayerCharacter


def test_character_creation():
    c = PlayerCharacter()
    assert c is not None


def test_character_to_dict():
    c = PlayerCharacter()
    d = c.to_dict()
    assert isinstance(d, dict)


def test_character_has_expected_attrs():
    c = PlayerCharacter()
    assert hasattr(c, "level")
    assert hasattr(c, "bio")
    assert hasattr(c, "abilities")
    assert hasattr(c, "hp")
    assert hasattr(c, "ac")
    assert hasattr(c, "equipment")
