def getInput():
    with open("input.txt", "r") as inp:
        lines = [x for x in inp.read().split("\n")]
        inp.close()
    return lines

def getBounds(line):
    boundaries = line.split(" ", 1)[0]
    res = [int(x) for x in boundaries.split("-", 1)]
    res.sort()
    return res

def getLetter(line):
    removeFirst = line.split(" ", 1)[1]
    return removeFirst.split(":", 1)[0]

def getPassword(line):
    withSpace = line.split(":", 1)[1]
    return withSpace[1 : : ]

def puzzleOne():
    valid = 0
    lines = getInput()
    for line in lines:
        boundaries = getBounds(line)
        letter = getLetter(line)
        password = getPassword(line)
        count = password.count(letter)
        if(count <= boundaries[1] and count >= boundaries[0]):
            valid+=1
    print(valid)

def puzzleTwo():
    valid = 0
    lines = getInput()
    for line in lines:
        boundaries = getBounds(line)
        letter = getLetter(line)
        password = getPassword(line)
        print("Checking: Boundaries %s with password %s for character %s" % (boundaries, password, letter))
        if((password[boundaries[0] - 1] == letter) != (password[boundaries[1] - 1] == letter)):
            valid += 1
        else:
            print("INVALID ^^")

    print(valid)

puzzleTwo()