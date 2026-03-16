from rpg_tools.maze_rats.magic import generate_spell


def test_generate_spell_returns_string():
    assert isinstance(generate_spell(), str)


def test_generate_spell_two_words():
    spell = generate_spell()
    parts = spell.split()
    assert len(parts) == 2


def test_generate_spell_variety():
    spells = {generate_spell() for _ in range(100)}
    assert len(spells) > 1
