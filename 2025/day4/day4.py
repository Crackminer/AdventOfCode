puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2025/day4/day4.txt', 'r') as file:
    puzzleinput = file.read()

testinput = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def checkSurround(lines, i, j, toFind):
    surrounding = 0
    if i - 1 >= 0 and j - 1 >= 0 and lines[i-1][j-1] == toFind:
        surrounding += 1
    if i - 1 >= 0 and lines[i-1][j] == toFind:
        surrounding += 1
    if i - 1 >= 0 and j + 1 < len(lines[i - 1]) and lines[i-1][j+1] == toFind:
        surrounding += 1
    if j - 1 >= 0 and lines[i][j-1] == toFind:
        surrounding += 1
    if j + 1 < len(lines[i]) and lines[i][j+1] == toFind:
        surrounding += 1
    if i + 1 < len(lines) and j - 1 >= 0 and lines[i+1][j-1] == toFind:
        surrounding += 1
    if i + 1 < len(lines) and lines[i+1][j] == toFind:
        surrounding += 1
    if i + 1 < len(lines) and j + 1 < len(lines[i + 1]) and lines[i+1][j+1] == toFind:
        surrounding += 1
    return surrounding

def getIndexes(lines, toFind):
    indexes = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == toFind: 
                if checkSurround(lines, i, j, toFind) < 4:
                    indexes.append((i, j))
    return indexes

def replaceIndexes(lines, indexes, replacement):
    for i, j in indexes:
        lines[i] = lines[i][:j] + replacement + lines[i][j+1:]
    return lines

def part1():
    #puzzleinput = testinput
    lines = puzzleinput.splitlines()
    print(len(getIndexes(lines, '@')))

def part2():
    #puzzleinput = testinput
    lines = puzzleinput.splitlines()

    sum = 0

    while True:
        indexes = getIndexes(lines, '@')
        sum += len(indexes)
        if len(indexes) == 0:
            break
        lines = replaceIndexes(lines, indexes, '.')

    print(sum)

part1()
part2()