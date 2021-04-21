def mod_to_str(mod: int) -> str:
    if mod >= 0:
        mod_str = f"+{mod}"
    else:
        mod_str = f"{mod}"
    return mod_str


def dot_pad(s: str, chars: int) -> str:
    n = chars - len(s)
    return "." * n


def mods_5e(score: int) -> int:
    mod = score // 2 - 5
    return mod


def mods_bx(score: int) -> int:
    if score == 3:
        mod = -3
    elif score in range(4, 6):
        mod = -2
    elif score in range(6, 9):
        mod = -1
    elif score in range(9, 13):
        mod = 0
    elif score in range(13, 16):
        mod = 1
    elif score in range(16, 18):
        mod = 2
    elif score == 18:
        mod = 3
    else:
        raise Exception("Score outside valid range 3-18")
    return mod
