def getInput():
    with open("input.txt", "r") as inp:
        lines = [x for x in inp.read().split("\n")]
        inp.close()
    return lines


def getRow(line):
    rowChars = line[0:7]
    rows = [i for i in range(0, 128)]
    for char in rowChars:
        if(char == "F"):
            rows = rows[0:len(rows) / 2]
        elif(char == "B"):
            rows = rows[len(rows) / 2:len(rows)]
        else:
            raise Exception("Invalid Character in Row!")
        if(len(rows) == 1):
            break
    if(len(rows) == 1):
        return rows[0]
    else:
        print(rows)
        raise Exception("Row length is greater than one!")


def getColumn(line):
    columnChars = line[7:11]
    print(columnChars)
    columns = [i for i in range(0, 8)]
    for char in columnChars:
        print(columns)
        if(char == "L"):
            columns = columns[0:len(columns) / 2]
        elif(char == "R"):
            columns = columns[len(columns) / 2:len(columns)]
        else:
            raise Exception("Invalid Character in Column")
        if(len(columns) == 1):
            break
    if(len(columns) == 1):
        return columns[0]
    else:
        print(columns)
        raise Exception("Column length is not equal to one!")


def puzzleOne():
    lines = getInput()
    highest = 0
    for line in lines:
        row = getRow(line)
        column = getColumn(line)
        seatId = (row * 8) + column
        if(seatId >= highest):
            highest = seatId
    print(highest)


def puzzleTwo():
    lines = getInput()
    seatsFound = []
    for line in lines:
        row = getRow(line)
        column = getColumn(line)
        seatId = (row * 8) + column
        if(seatId not in seatsFound):
            seatsFound.append(seatId)
    seatsFound.sort()
    for i in range(0, len(seatsFound)):
        if(seatsFound[i + 1] != seatsFound[i] + 1):
            print("Seat is %s" % (seatsFound[i] + 1))
            break


puzzleOne()
puzzleTwo()
