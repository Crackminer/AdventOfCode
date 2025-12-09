puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2025/day7/day7.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

testinput = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

def sharedFunc():
    #puzzleinput = testinput

    lines = puzzleinput.splitlines()

    curr = [0]*len(lines[0])
    curr[lines[0].index('S')]=1

    splitcount, timelinecount = 0, 1
    for i in lines[1:]:
        for col in range(len(curr)):
            if curr[col] > 0 and i[col] == '^':
                splitcount += 1
                timelinecount += curr[col]
                curr[col-1] += curr[col]
                curr[col+1] += curr[col]
                curr[col] = 0
                
    return splitcount, timelinecount

def part1():
    print(sharedFunc()[0])

def part2():
    print(sharedFunc()[1])

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")