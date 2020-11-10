

def mod_to_str(mod: int) -> str:
    if mod >= 0:
        mod_str = f"+{mod}"
    else:
        mod_str = f"{mod}"
    return mod_str


def dot_pad(s: str, chars: int) -> str:
    n = chars - len(s)
    return '.' * n
