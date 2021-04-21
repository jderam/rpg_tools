import random


def roll_dice(n: int, s: int) -> int:
    result = 0
    for i in range(n):
        result += random.randint(1, s)
    return result


def roll_ndn_drop_n(n: int, s: int, d: int) -> int:
    results = []
    for i in range(n):
        results.append(random.randint(1, s))
    results.sort(reverse=True)
    # print(results)
    results = results[:-d]
    return sum(results)
