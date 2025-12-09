puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2024/day3/day3.txt', 'r') as file:
    puzzleinput = file.read()

from datetime import datetime

# heavily modified the day3.txt input, made newline before each mul and do, which significantly simplifies the task

def part1():
    sum = 0
    for line in puzzleinput.split('\n'):
        if line.startswith('mul('):
            occurence = line.find(')')
            if occurence == -1:
                continue
            substring = line[4:occurence]
            occurence = substring.find(',')
            if occurence == -1:
                continue
            split = substring.split(',')
            try:
                int1 = int(split[0])
                int2 = int(split[1])
                sum += int1 * int2
            except:
                continue
    print(sum)

def part2():
    sum = 0
    do = True
    for line in puzzleinput.split('\n'):
        if line.startswith('mul('):
            if not do:
                continue
            occurence = line.find(')')
            if occurence == -1:
                continue
            substring = line[4:occurence]
            occurence = substring.find(',')
            if occurence == -1:
                continue
            split = substring.split(',')
            try:
                int1 = int(split[0])
                int2 = int(split[1])
                sum += int1 * int2
            except:
                continue
        if line.startswith('do()'):
            do = True
        if line.startswith('don\'t()'):
            do = False
    print(sum)

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")