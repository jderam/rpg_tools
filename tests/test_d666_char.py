from rpg_tools.d666.char import D666Character


def test_character_creation():
    c = D666Character()
    assert hasattr(c, "name")
    assert hasattr(c, "level")
    assert hasattr(c, "hit_points")
    assert hasattr(c, "skills")
    assert hasattr(c, "extraordinary_abilities")
    assert hasattr(c, "weapon")
    assert hasattr(c, "equipment")
    assert hasattr(c, "background")
    assert hasattr(c, "spells")
    assert hasattr(c, "money")


def test_character_to_dict():
    c = D666Character()
    d = c.to_dict()
    assert isinstance(d, dict)
    assert "name" in d
    assert "level" in d
    assert "hit_points" in d


def test_character_levels():
    for level in range(1, 6):
        c = D666Character(level=level)
        assert c.hit_points >= 3
        assert c.level == level
