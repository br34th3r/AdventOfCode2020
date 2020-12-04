import string

def getInput():
    with open("input.txt", "r") as inp:
        lines = [x for x in inp.read().split("\n")]
        inp.close()
    return lines

def groupPassports(lines):
    strPassports = groupLines(lines)
    passports = []
    for line in strPassports:
        passport = {}
        spaces = line.split(" ")
        for val in spaces:
            final = val.split(":")
            passport[final[0]] = final[1]
        passports.append(passport)
    return passports

def groupLines(lines):
    currentLine = ""
    passports = []
    for line in lines:
        if(line != ""):
            currentLine += line + " "
        else:
            currentLine = currentLine[:-1]
            passports.append(currentLine)
            currentLine = ""
    currentLine = currentLine[:-1]
    passports.append(currentLine)
    currentLine = ""
    return passports

def puzzleOne():
    lines = getInput()
    passports = groupPassports(lines)
    valid = 0
    validPassports = []
    for passport in passports:
        if(passport.keys() >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}):
            valid += 1
            validPassports.append(passport)
    print(valid)
    return validPassports

def checkBYR(value):
    if(len(value) == 4):
        if(int(value) >= 1920 and int(value) <= 2002):
            return True
        else:
            return False
    else:
        return False

def checkIYR(value):
    if(len(value) == 4):
        if(int(value) >= 2010 and int(value) <= 2020):
            return True
        else:
            print("FAILED AT IYR - Not in Range")
            return False
    else:
        print("FAILED AT IYR - Bad Length")
        return False

def checkEYR(value):
    if(len(value) == 4):
        if(int(value) >= 2020 and int(value) <= 2030):
            return True
        else:
            print("FAILED AT EYR - Not in Range")
            return False
    else:
        print("FAILED AT EYR - Bad Length")
        return False

def checkHGT(value):
    for i, char in enumerate(value):
        if not char.isdigit():
            break
    number = int(value[:i])
    units = value[i:]
    print("HGT %s %s" % (str(number), str(units)))
    if(units == "cm"):
        if(number >= 150 and number <= 193):
            return True
        else:
            print("FAILED AT HGT - Not in Range")
            return False
    elif(units == "in"):
        if(number >= 59 and number <= 76):
            return True
        else:
            print("FAILED AT HGT - Not in Range")
            return False
    else:
        print("FAILED AT HGT")
        return False

def checkHCL(value):
    if(len(value) == 7 and value[0] == "#"):
        try:
            return all(char in string.hexdigits for char in value[1:])
        except:
            print("FAILED AT HCL")
            return False
    else:
        print("FAILED AT HCL")
        return False

def checkECL(value):
    if(value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return True
    else:
        print("FAILED AT ECL")
        return False

def checkPID(value):
    if(len(value) == 9):
        for char in value:
            if(not char.isdigit()):
                print("FAILED AT PID")
                return False
        return True

def runChecks(passport):
    try:
        if(checkBYR(passport['byr']) and checkECL(passport['ecl']) and checkHCL(passport['hcl']) and checkHGT(passport['hgt']) and checkEYR(passport['eyr']) and checkIYR(passport['iyr']) and checkPID(passport['pid'])):
            return True
        else:
            return False
    except KeyError:
        return False

        

def puzzleTwo():
    passports = puzzleOne()
    valid = 0
    for passport in passports:
        print(passport)
        if(runChecks(passport)):
            valid += 1
    print(valid)

puzzleOne()
puzzleTwo()