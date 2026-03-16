from rpg_tools.assh.char import PlayerCharacter


def test_character_creation():
    c = PlayerCharacter()
    assert hasattr(c, "char_class")
    assert hasattr(c, "abilities")
    assert hasattr(c, "hp")
    assert hasattr(c, "ac")


def test_character_class_choices():
    classes = {"Fighter", "Thief", "Magician", "Cleric"}
    for _ in range(50):
        c = PlayerCharacter()
        assert c.char_class in classes


def test_character_to_dict_and_to_json():
    c = PlayerCharacter()
    d = c.to_dict()
    assert isinstance(d, dict)
    j = c.to_json()
    assert isinstance(j, str)


def test_character_dying_earth_spells():
    c = PlayerCharacter(magician_spell_src="dying_earth")
    assert hasattr(c, "spell_list")
