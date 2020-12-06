def getInput():
    with open("input.txt", "r") as inp:
        lines = [x for x in inp.read().split("\n")]
        inp.close()
    return lines


def puzzleOne():
    lines = getInput()
    groups = []
    currentGroup = []
    for line in lines:
        if(line != ""):
            for char in line:
                if(not char in currentGroup):
                    currentGroup.append(char)
        else:
            groups.append(currentGroup)
            currentGroup = []
    groups.append(currentGroup)
    counts = [len(i) for i in groups]
    print(sum(counts))


def puzzleTwo():
    lines = getInput()
    groups = []
    currentGroup = []
    people = 0
    counts = []
    for line in lines:
        if(line != ""):
            people += 1
            for char in line:
                currentGroup.append(char)
        else:
            currentGroup.append(people)
            groups.append(currentGroup)
            currentGroup = []
            people = 0
    currentGroup.append(people)
    groups.append(currentGroup)
    for group in groups:
        people = group[len(group) - 1]
        currentCount = []
        for i in range(0, len(group) - 1):
            if(group.count(group[i]) == people and not group[i] in currentCount):
                currentCount.append(group[i])
        counts.append(currentCount)
    print(sum([len(i) for i in counts]))


puzzleOne()
puzzleTwo()
