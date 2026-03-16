import pytest

from rpg_tools.utils.dice import roll_dice, roll_ndn_drop_n


def test_roll_dice_returns_int():
    assert isinstance(roll_dice(2, 6), int)


@pytest.mark.repeat(100)
def test_roll_dice_range():
    result = roll_dice(2, 6)
    assert 2 <= result <= 12


def test_roll_ndn_drop_n_returns_int():
    assert isinstance(roll_ndn_drop_n(4, 6, 1), int)


@pytest.mark.repeat(100)
def test_roll_ndn_drop_n_range():
    result = roll_ndn_drop_n(4, 6, 1)
    assert 3 <= result <= 18
