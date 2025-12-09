puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day9/day9.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

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
    try:
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
    except:
        return collapsed

def collapsepart2(list :list) -> list:
    collapsed = []
    try:
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
                        if findblock * -1 >= i:
                            return collapsed
                        blocklength = 1
                        while (findblock - blocklength) * -1 < len(list) and list[findblock - blocklength] != -1:
                            blocklength += 1
                        if blocklength <= blockcount:
                            # get the found block from the back inside the block at the beginning
                            collapsed.extend(list[findblock - blocklength:findblock])
                            for j in range(blocklength):
                                list[findblock - j] = -1
                            break
            else:
                collapsed.append(list[i])
        return collapsed
    except:
        return collapsed

def part1():
    inputlist = []
    input = testinput   # changed to testinput for part 2 as puzzleinput takes about 5-10 seconds and i dont want to wait on that
    for char in input:
        inputlist.append(int(char))
    
    bloated = bloat(inputlist)
    collapsed = collapse(bloated)
    print(getsum(collapsed))

def part2():
    # Thank you u/4HbQ on Reddit for the solution, found in this post: https://www.reddit.com/r/adventofcode/comments/1ha27bo/2024_day_9_solutions/
    D = [(i//2+1 if i%2 else 0, int(d)) for i,d in enumerate(puzzleinput, 1)]

    for i in range(len(D))[::-1]:
        for j in range(i):
            i_data, i_size = D[i]
            j_data, j_size = D[j]

            if i_data and not j_data and i_size <= j_size:
                D[i] = (0, i_size)
                D[j] = (0, j_size - i_size)
                D.insert(j, (i_data, i_size))


    flatten = lambda x: [x for x in x for x in x]

    print(sum(i*(c-1) for i,c in enumerate(flatten([d]*s for d,s in D)) if c))



print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")