testinput = """3   4\n4   3\n2   5\n1   3\n3   9\n3   3"""

from datetime import datetime

def part1():
    input = testinput
    with open('2024/day1/day1.txt', 'r') as file:
        input = file.read()
    leftlist = []
    rightlist = []
    splitinput = input.split('\n')

    for numstrings in splitinput:
        numbers = numstrings.split("   ")
        leftlist.append(int(numbers[0]))
        rightlist.append(int(numbers[1]))

    leftlist.sort()
    rightlist.sort()
    totaldistance = 0

    for i in range(0, len(leftlist)):
        tmp = rightlist[i] - leftlist[i]
        if tmp < 0:
            tmp *= -1
        totaldistance += tmp
    
    print(f"The total distance is {totaldistance}")

def part2():
    input = testinput
    with open('2024/day1/day1.txt', 'r') as file:
        input = file.read()
    leftlist = []
    rightlist = []
    splitinput = input.split('\n')

    for numstrings in splitinput:
        numbers = numstrings.split("   ")
        leftlist.append(int(numbers[0]))
        rightlist.append(int(numbers[1]))

    similarities = 0

    for i in range(0, len(leftlist)):
        tmp = leftlist[i] * rightlist.count(leftlist[i])
        similarities += tmp
    
    print(f"The total similarities are {similarities}")


print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")