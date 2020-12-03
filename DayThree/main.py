def getInput():
    with open("DayThree/input.txt", "r") as inp:
        lines = [x for x in inp.read().split("\n")]
        inp.close()
    return lines

def getNextPosition(currentX, currentY, right, down, lines):
    newY = currentY + down
    newX = (currentX + right) % len(lines[0])
    return newX, newY

def isTree(x, y, lines):
    if(lines[y][x] == "#"):
        return True
    else:
        return False

def runSlope(right, down):
    lines = getInput()
    x = 0
    y = 0
    trees = 0
    for i in range(0, len(lines) - 1, down):
        x, y = getNextPosition(x, y, right, down, lines)
        if(isTree(x, y, lines)):
            trees += 1
    return trees

def puzzleOne():
    lines = getInput()
    x = 0
    y = 0
    trees = 0
    for i in range(0, len(lines) - 1):
        x, y = getNextPosition(x, y, 3, 1, lines)
        if(isTree(x, y, lines)):
            trees += 1
    print(trees)
    return trees

def puzzleTwo():
    val = runSlope(1, 1) * puzzleOne() * runSlope(5, 1) * runSlope(7, 1) * runSlope(1, 2)
    print(val)

puzzleOne()
puzzleTwo()