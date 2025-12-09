puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day1/day1.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

def part1():
    floor = 0
    for i in range(0, len(puzzleinput)):
        if puzzleinput[i] == '(':
            floor += 1
        elif puzzleinput[i] == ')':
            floor -= 1
    print(f'The floor is {floor}')

def part2():
    floor = 0
    for i in range(0, len(puzzleinput)):
        if puzzleinput[i] == '(':
            floor += 1
        elif puzzleinput[i] == ')':
            floor -= 1
        if floor == -1:
            print(f'The position is {i+1}')
            break

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")