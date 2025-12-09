import progressbar
from sympy import divisors
from datetime import datetime


puzzleinput :str        # done to initialize an empty variable, without the :str it would be an error
with open('2015/day20/day20.txt', 'r') as file:
    puzzleinput = file.read()

def calculate_presents(house_number, presents_per_house, limit: int = None) -> int:
    if limit:
        visits = sum(elf for elf in divisors(house_number) if house_number <= elf * limit)
    else:
        visits = sum(divisors(house_number))
    return visits * presents_per_house


def part1():
    target = int(puzzleinput)
    house_number = 1
    p = progressbar.ProgressBar(widgets=[progressbar.Percentage(), progressbar.Bar()], maxval=776160)
    p.start()
    while calculate_presents(house_number, 10) < target:
        house_number += 1
        p.update(house_number)
    p.finish()
    print(house_number)


def part2():
    target = int(puzzleinput)
    house_number = 1
    p = progressbar.ProgressBar(widgets=[progressbar.Percentage(), progressbar.Bar()], maxval=786240)
    p.start()
    while calculate_presents(house_number, 11, 50) < target:
        house_number += 1
        p.update(house_number)
    p.finish()
    print(house_number)

print(f"{datetime.now()}: Started executing part1.")
part1()
print(f"{datetime.now()}: Ended executing part1.")
print(f"{datetime.now()}: Started executing part2.")
part2()
print(f"{datetime.now()}: Ended executing part2.")