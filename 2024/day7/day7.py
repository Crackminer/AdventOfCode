puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day7/day7.txt', 'r') as file:
    puzzleinput = file.read()

testinput = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def getpossibleresults(list :list) -> list:
    if len(list) == 1:
        return list
    results = getpossibleresults(list[:-1])
    newresults = []
    for result in results:
        newresults.append(list[-1] * result)
        newresults.append(list[-1] + result)
    return newresults

def possible(list :list) -> bool:
    target = list[0]
    results = getpossibleresults(list[1])
    return target in results
    
def getpossibleresultspart2(list :list) -> list:
    if len(list) == 1:
        return list
    results = getpossibleresultspart2(list[:-1])
    newresults = []
    for result in results:
        newresults.append(list[-1] * result)
        newresults.append(list[-1] + result)
        newresults.append(int(f'{result}{list[-1]}'))
    return newresults

def possiblepart2(list :list) -> bool:
    target = list[0]
    results = getpossibleresultspart2(list[1])
    return target in results

def part1():
    input = puzzleinput
    equations = []
    for line in input.split('\n'):
        solution = line.split(': ')[0]
        numbers = []
        for numchar in line.split(': ')[1].split(' '):
            numbers.append(int(numchar))
        equations.append([int(solution), numbers])
    totalsum = 0
    for equation in equations:
        if possible(equation):
            totalsum += equation[0]
    print(totalsum)

def part2():
    input = puzzleinput
    equations = []
    for line in input.split('\n'):
        solution = line.split(': ')[0]
        numbers = []
        for numchar in line.split(': ')[1].split(' '):
            numbers.append(int(numchar))
        equations.append([int(solution), numbers])
    totalsum = 0
    for equation in equations:
        if possiblepart2(equation):
            totalsum += equation[0]
    print(totalsum)
    print()

part1()
part2()