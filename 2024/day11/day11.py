puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day11/day11.txt', 'r') as file:
    puzzleinput = file.read()

testinput = "125 17"

def blink(list :list) -> None:
    newlist = []
    for element in list:
        if element == 0:
            newlist.append(1)
        elif len(str(element)) % 2 == 0:
            string = str(element)
            newlist.append(int(string[:int(len(string) / 2)]))
            newlist.append(int(string[int(len(string) / 2):]))
        else:
            newlist.append(element * 2024)
    return newlist

def part1():
    input = puzzleinput
    list = []
    for numstring in input.split(' '):
        list.append(int(numstring))
    for i in range(25):
        list = blink(list)
    print(len(list))

def part2():
    input = puzzleinput
    list = []
    for numstring in input.split(' '):
        list.append(int(numstring))
    for i in range(75):
        list = blink(list)
    print(len(list))

part1()
part2()