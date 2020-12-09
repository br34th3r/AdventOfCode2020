def getInput():
    with open("input.txt", "r") as inp:
        lines = [int(x) for x in inp.read().split("\n")]
        inp.close()
    return lines

def puzzleOne():
    lines = getInput()
    data = []
    for number in lines:
        if(len(data) != 25):
            data.append(number)
        else:
            valueFound = False
            for i, num1 in enumerate(data):
                for j, num2 in enumerate(data):
                    if(i == j):
                        pass
                    elif(num1 + num2 == number):
                        valueFound = True
            if(not valueFound):
                print(number)
                return number
            else:
                data.pop(0)
                data.append(number)
    return Exception("Your values were... fine...?")

def puzzleTwo(invalid):
    lines = getInput()
    for i, number in enumerate(lines):
        positions = 0
        total = 0
        while(total != invalid):
            positions += 1
            total = sum(lines[i:i+positions])
            if(total < invalid):
                continue
            elif(total > invalid):
                break
            else:
                return sum([min(lines[i:i+positions]), max(lines[i:i+positions])])
        
print(puzzleTwo(puzzleOne()))