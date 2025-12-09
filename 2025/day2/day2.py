puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2025/day2/day2.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

testinput = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

def invalid(num :int) -> bool:
    strnum = str(num)
    if (len(strnum) % 2 == 1):
        return False
    
    middle = int(len(strnum) / 2)

    if strnum[0:middle] == strnum[middle:]:
        return True
    return False

def invalidPart2(num :int) -> bool:
    strnum = str(num)

    for i in range(1, len(strnum)):
        if len(strnum) % i == 0 and strnum[:i] * (len(strnum) // i) == strnum:
            return True
    return False


def part1():
    #puzzleinput = testinput
    ids = puzzleinput.split(",")
    invalidsum = 0
    for idpair in ids:
        vals = idpair.split("-")
        numid1 = int(vals[0])
        numid2 = int(vals[1])

        for i in range(numid1, numid2 + 1):
            if invalid(i):
                invalidsum += i
    print(invalidsum)

def part2():
    #puzzleinput = testinput
    ids = puzzleinput.split(",")
    invalidsum = 0
    for idpair in ids:
        vals = idpair.split("-")
        numid1 = int(vals[0])
        numid2 = int(vals[1])

        for i in range(numid1, numid2 + 1):
            if invalidPart2(i):
                invalidsum += i
    print(invalidsum)

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")