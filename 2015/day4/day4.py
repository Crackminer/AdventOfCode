import hashlib

puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day4/day4.txt', 'r') as file:
    puzzleinput = file.read()

def part1():
    number = 0
    while True:
        md5unhashed = puzzleinput + str(number)
        md5 = hashlib.md5(md5unhashed.encode()).hexdigest()
        if (md5.startswith("00000")):
            break
        number += 1
    print(f"The number for the has generation is {number}.")

def part2():
    number = 0
    while True:
        md5unhashed = puzzleinput + str(number)
        md5 = hashlib.md5(md5unhashed.encode()).hexdigest()
        if (md5.startswith("000000")):
            break
        number += 1
    print(f"The number for the has generation is {number}.")

part1()
part2()