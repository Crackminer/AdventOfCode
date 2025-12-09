import itertools
from datetime import datetime

puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day17/day17.txt', 'r') as file:
    puzzleinput = file.read()

def getcontainers(input :str) -> list:
    list = []
    for line in input.split('\n'):
        list.append(int(line))
    return list

def part1():
    list = getcontainers(puzzleinput)
    combos = []
    for i in range(len(list)):
        for combo in itertools.combinations(list, i):
            if sum(combo) == 150:
                combos.append(combo)
    print(len(combos))

def part2():
    list = getcontainers(puzzleinput)
    combosinit = []
    for i in range(len(list)):
        for combo in itertools.combinations(list, i):
            if sum(combo) == 150:
                combosinit.append(combo)
    leastcontainers = 10000
    for combo in combosinit:
        if len(combo) < leastcontainers:
            leastcontainers = len(combo)
    combos = []
    for i in range(len(list)):
        for combo in itertools.combinations(list, i):
            if sum(combo) == 150 and len(combo) == leastcontainers:
                combos.append(combo)
    print(len(combos))

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")