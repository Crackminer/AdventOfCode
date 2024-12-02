# unique take on getting the strings our of the file, once again thanks to TessFerrandez (https://github.com/TessFerrandez/AdventOfCode-Python/blob/develop/2015/day8.py)
def parse_input():
    return [line.strip() for line in open('2015/day8/day8.txt').readlines()]

def part1():
    input = parse_input()
    countfull = 0
    countreduced = 0
    for line in input:
        countfull += len(line)
        countreduced += len(bytes(line[1:-1], "utf-8").decode('unicode-escape'))
    print(countfull - countreduced)

def part2():
    input = parse_input()
    countfull = 0
    countfuller = 0
    for line in input:
        countfull += len(line)
        countfuller += len(line)
        countfuller += line.count('"')
        countfuller += line.count("'")
        countfuller += line.count("\\")
        countfuller += 2
    print(countfuller - countfull)

part1()
part2()