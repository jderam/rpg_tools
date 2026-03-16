import pytest

from rpg_tools.utils.misc import dot_pad, mod_to_str, mods_5e, mods_bx


def test_mod_to_str_positive():
    assert mod_to_str(3) == "+3"


def test_mod_to_str_zero():
    assert mod_to_str(0) == "+0"


def test_mod_to_str_negative():
    assert mod_to_str(-2) == "-2"


def test_dot_pad():
    result = dot_pad("HP", 10)
    assert result == "." * 8


def test_mods_5e():
    assert mods_5e(10) == 0
    assert mods_5e(18) == 4
    assert mods_5e(3) == -4


def test_mods_bx():
    assert mods_bx(3) == -3
    assert mods_bx(5) == -2
    assert mods_bx(8) == -1
    assert mods_bx(10) == 0
    assert mods_bx(14) == 1
    assert mods_bx(17) == 2
    assert mods_bx(18) == 3


def test_mods_bx_invalid():
    with pytest.raises(Exception):
        mods_bx(2)
    with pytest.raises(Exception):
        mods_bx(19)
