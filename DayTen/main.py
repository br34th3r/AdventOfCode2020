from functools import lru_cache
used = []
differences = []


def getInput():
    with open("input.txt", "r") as inp:
        lines = [int(x) for x in inp.read().split("\n")]
        inp.close()
    return lines


adapters = getInput()


def getAdapter(val, adapters):
    return [x for x in adapters if (
        x != val) and (x - val <= 3 and x - val > 0)]


@lru_cache
def combinations(start):
    if(start == max(adapters)):
        return 1
    total = 0
    for val in getAdapter(start, adapters):
        total += combinations(val)
    return total


def getNextAdapter(current, adapters):
    global used, differences
    usable = [x for x in adapters if (not x in used and x - current <= 3)]
    differences.append(min(usable) - current)
    used.append(min(usable))
    if(not len(used) >= len(adapters)):
        getNextAdapter(min(usable), adapters)
    else:
        used.append(max(adapters) + 3)
        differences.append(3)


def puzzleOne():
    lines = getInput()
    getNextAdapter(0, lines)
    print(differences.count(1) * differences.count(3))


def puzzleTwo():
    lines = getInput()
    lines.sort()
    lines = set(lines)
    print(combinations(0))


puzzleOne()
puzzleTwo()
