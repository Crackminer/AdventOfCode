puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day9/day9.txt', 'r') as file:
    puzzleinput = file.read()

testinput = "2333133121414131402"

def getsum(list :list) -> int:
    sum = 0
    for i in range(len(list)):
        sum += i * list[i]
    return sum

def bloat(input :list) -> list:
    output = []
    for i in range(len(input)):
        helper = input[i]
        while helper != 0:
            if i % 2 == 0:
                output.append(int(i / 2))
            else:
                output.append(-1)
            helper -= 1
    return output

def collapse(list :list) -> list:
    collapsed = []
    for i in range(len(list)):
        if list[i] == -1:
            while list[-1] == -1:
                list = list[:-1] 
            if len(list) <= len(collapsed):
                break
            collapsed.append(list[-1])
            list = list[:-1] 
        else:
            collapsed.append(list[i])
    return collapsed

def collapsepart2(list :list) -> list:
    collapsed = []
    for i in range(len(list)):
        if list[i] == -1:
            blockcount = 1
            while i + blockcount < len(list) and list[i + blockcount] == -1:
                blockcount += 1
            while blockcount > 0:
                findblock = -1
                while True:
                    while list[findblock] == -1:
                        findblock -= 1
                    blocklength = 1
                    while (findblock - blocklength) * -1 < len(list) and list[findblock - blocklength] != -1:
                        blocklength += 1
                    if blocklength <= blockcount:
                        # get the found block from the back inside the block at the beginning
                        break

def part1():
    inputlist = []
    input = puzzleinput
    for char in input:
        inputlist.append(int(char))
    
    bloated = bloat(inputlist)
    collapsed = collapse(bloated)
    print(getsum(collapsed))

def part2():
    print()

part1()
part2()