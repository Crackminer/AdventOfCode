puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day4/day4.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

#puzzleinput = """MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"""

def starsearch(list :list) -> int:
    count = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            # horizontal
            if j +3 < len(list[i]):
                if list[i][j] == 'X' and list[i][j+1] == 'M' and list[i][j+2] == 'A' and list[i][j+3] == 'S':
                    count += 1

            # reversed horizontal
            if j -3 >= 0:
                if list[i][j] == 'X' and list[i][j-1] == 'M' and list[i][j-2] == 'A' and list[i][j-3] == 'S':
                    count += 1

            # vertical
            if i+3 < len(list):
                if list[i][j] == 'X' and list[i+1][j] == 'M' and list[i+2][j] == 'A' and list[i+3][j] == 'S':
                    count += 1

            # reversed vertical
            if i-3 >= 0:
                if list[i][j] == 'X' and list[i-1][j] == 'M' and list[i-2][j] == 'A' and list[i-3][j] == 'S':
                    count += 1

            # forward down diagonal
            if i +3 < len(list) and j +3 < len(list[i]):
                if list[i][j] == 'X' and list[i+1][j+1] == 'M' and list[i+2][j+2] == 'A' and list[i+3][j+3] == 'S':

                    count += 1

            # reverse down diagonal
            if i +3 < len(list) and j -3 >= 0:
                if list[i][j] == 'X' and list[i+1][j-1] == 'M' and list[i+2][j-2] == 'A' and list[i+3][j-3] == 'S':
                    count += 1

            # forward up diagonal
            if i -3 >= 0 and j +3 < len(list[i]):
                if list[i][j] == 'X' and list[i-1][j+1] == 'M' and list[i-2][j+2] == 'A' and list[i-3][j+3] == 'S':
                    count += 1

            # reverse up diagonal
            if i -3 >= 0 and j -3 >= 0:
                if list[i][j] == 'X' and list[i-1][j-1] == 'M' and list[i-2][j-2] == 'A' and list[i-3][j-3] == 'S':
                    count += 1
    return count

def xshapedmassearch(list :list) -> int:
    count = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if i+2 < len(list) and j+2 < len(list[i]):
                
                # M . M
                # . A .
                # S . S
                
                if list[i][j] == 'M' and list[i][j+2] == 'M' and list[i+1][j+1] == 'A' and list[i+2][j] == 'S' and list[i+2][j+2] == 'S':
                    count += 1
                
                # M . S
                # . A .
                # M . S

                if list[i][j] == 'M' and list[i][j+2] == 'S' and list[i+1][j+1] == 'A' and list[i+2][j] == 'M' and list[i+2][j+2] == 'S':
                    count += 1
                
                # S . S
                # . A .
                # M . M

                if list[i][j] == 'S' and list[i][j+2] == 'S' and list[i+1][j+1] == 'A' and list[i+2][j] == 'M' and list[i+2][j+2] == 'M':
                    count += 1

                # S . M
                # . A .
                # S . M

                if list[i][j] == 'S' and list[i][j+2] == 'M' and list[i+1][j+1] == 'A' and list[i+2][j] == 'S' and list[i+2][j+2] == 'M':
                    count += 1
    return count

def part1():
    input = []
    for line in puzzleinput.split('\n'):
        input.append(line)
    xmascount = 0
    xmascount += starsearch(input)
    print(xmascount)

def part2():
    input = []
    for line in puzzleinput.split('\n'):
        input.append(line)
    xmascount = 0
    xmascount += xshapedmassearch(input)
    print(xmascount)

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")