def getInput():
    with open("DayOne/input.txt", "r") as inp:
        nums = [int(x) for x in inp.read().split("\n")]
        inp.close()
    nums.sort()
    return nums


def findClosestIndex(arr, num):
    for i in range(0, len(arr)-2):
        if(arr[i+1] > num):
            return i
    return len(arr) - 1


def puzzleOne():
    nums = getInput()
    for val in nums:
        compare = 2020 - val
        if(compare in nums):
            print("Found a Match!")
            print("%s and %s" % (val, compare))
            print("Answer is: %s" % (val * compare))


def puzzleTwo():
    nums = getInput()
    for val in nums:
        compare = 2020 - val
        nums = nums[0:findClosestIndex(nums, compare)]
        for check in nums:
            secondCompare = compare - check
            if(secondCompare in nums):
                print("Found a Match!")
                print("%s, %s and %s" % (val, check, secondCompare))
                print("Answer is: %s" % (val * check * secondCompare))
            else:
                nums = getInput()


puzzleOne()
puzzleTwo()
