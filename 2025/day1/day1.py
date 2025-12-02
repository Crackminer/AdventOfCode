puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2025/day1/day1.txt', 'r') as file:
    puzzleinput = file.read()

testinput = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

def part1():
    #puzzleinput = testinput
    actual = 50
    zeroCount = 0
    for line in puzzleinput.splitlines():
        instruction = line[0]
        move = int(line[1:]) if instruction == 'R' else int(line[1:]) * -1

        actual += move
        while actual < 0:
            actual += 100
        while actual > 99:
            actual -= 100
        if actual == 0:
            zeroCount += 1
    print(zeroCount)

def part2():
    #puzzleinput = testinput
    actual = 50
    zeroCount = 0
    for line in puzzleinput.splitlines():
        instruction = line[0]
        move = int(line[1:]) if instruction == 'R' else int(line[1:]) * -1

        overshot = abs(move) // 100
        zeroCount += overshot
        if move > 0 :
            move = move - overshot * 100
        if move < 0 :
            move = move + overshot * 100
        if move % 100 == 0 :
            actual = newactual
            continue
        if move < 0 and actual != 0 and actual + move <= 0:
            zeroCount += 1
        if move > 0 and move + actual >= 100:
            zeroCount += 1
        newactual = (actual + move) % 100
        actual = newactual
    print(zeroCount)

part1()
part2()