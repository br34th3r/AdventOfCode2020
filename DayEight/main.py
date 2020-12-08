import sys

visited = []
accumulator = 0


def getInput():
    with open("input.txt", "r") as inp:
        lines = [x for x in inp.read().split("\n")]
        inp.close()
    return lines


def arrayInstructions(lines):
    instructions = []
    for instruction in lines:
        fun, value = instruction.split(" ")
        value = int(value)
        instructions.append([fun, value])
    return instructions


def runInstruction(instructions, i):
    global accumulator
    print("Running %s with value %s at position %s" %
          (instructions[i][0], instructions[i][1], i))
    if(i in visited):
        print(accumulator)
        sys.exit()
    else:
        visited.append(i)
        if(instructions[i][0] == "nop"):
            runInstruction(instructions, i+1)
        elif(instructions[i][0] == "acc"):
            accumulator += instructions[i][1]
            runInstruction(instructions, i+1)
        else:
            runInstruction(instructions, i + instructions[i][1])


def runProgram(instructions, i):
    global accumulator
    if(instructions[i][0] == "nop"):
        runProgram(instructions, i+1)
    elif(instructions[i][0] == "acc"):
        accumulator += instructions[i][1]
        runProgram(instructions, i+1)
    elif(instructions[i][0] == "jmp"):
        runProgram(instructions, i + instructions[i][1])
    else:
        raise Exception("Invalid Argument")


def puzzleOne():
    lines = getInput()
    instructions = arrayInstructions(lines)
    runInstruction(instructions, 0)


def puzzleTwo():
    global accumulator
    lines = getInput()
    instructions = arrayInstructions(lines)
    for i, instruction in enumerate(instructions):
        if(instruction[0] == "jmp" or instruction[0] == "nop"):
            instructions[i][0] = "nop" if (
                instructions[i][0] == "jmp") else "jmp"
            accumulator = 0
            try:
                runProgram(instructions, 0)
            except IndexError:
                break
            except RecursionError:
                instructions[i][0] = "nop" if (
                    instructions[i][0] == "jmp") else "jmp"
    print(accumulator)


puzzleTwo()
