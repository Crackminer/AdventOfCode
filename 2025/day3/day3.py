puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2025/day3/day3.txt', 'r') as file:
    puzzleinput = file.read()

testinput = """987654321111111
811111111111119
234234234234278
818181911112111"""

def meanFunc(numdigits):
    #puzzleinput = testinput
    sum = 0
    for line in puzzleinput.splitlines():
        indexes = []
        for i in range(numdigits, 0, -1):
            curHigh = int(line[len(line)-i])
            index = len(line)-i
            for j in range(len(line)-i, numdigits-1-i, -1):
                indexes.sort()
                if int(line[j]) >= curHigh and (len(indexes) == 0 or j > indexes[-1]):
                    curHigh = int(line[j])
                    index = j
            indexes.append(index)
        num = 0
        indexes.sort()
        for index in indexes:
            num = num * 10 + int(line[index])
        sum += num

    print(sum)

def part1():
    meanFunc(2)

def part2():
    meanFunc(12)

part1()
part2()