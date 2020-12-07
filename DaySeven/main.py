bagsFound = []
internalBags = 0

def getInput():
    with open("input.txt", "r") as inp:
        lines = [x for x in inp.read().split("\n")]
        inp.close()
    return lines

def groupBags(lines):
    rules = {}
    for rule in lines:
        container, subbags = rule.split("contain")
        subbags = [x.strip() for x in subbags.split(",")]
        newRule = {}
        for bag in subbags:
            if(bag != "no other bags."):
                newRule[bag[2:]] = bag[0]
        rules[container.strip()] = newRule
    return rules

def findBag(rules, bag):
    global bagsFound
    for container in rules.keys():
        subBags = rules[container]
        for subBag in subBags.keys():
            if(bag in subBag):
                bagsFound.append(container)
                findBag(rules, container[:len(container) - 1])
                break

def findInternal(rules, bag, previous):
    global internalBags
    for subBag in rules[bag]:
            internalBags += int(rules[bag][subBag]) * previous
            if("bags." in subBag):
                findInternal(rules, subBag[:len(subBag) - 1], int(rules[bag][subBag]) * previous)
            elif("bags" in subBag):
                findInternal(rules, subBag, int(rules[bag][subBag]) * previous)
            elif("bag." in subBag):
                findInternal(rules, subBag[:len(subBag) - 1] + 's', int(rules[bag][subBag]) * previous)
            elif("bag" in subBag):
                findInternal(rules, subBag + "s", int(rules[bag][subBag]) * previous)

def puzzleOne():
    lines = getInput()
    rules = groupBags(lines)
    findBag(rules, "shiny gold bag")
    print(len(set(bagsFound)))

def puzzleTwo():
    lines = getInput()
    rules = groupBags(lines)
    findInternal(rules, "shiny gold bags", 1)
    print(internalBags)

puzzleOne()
puzzleTwo()